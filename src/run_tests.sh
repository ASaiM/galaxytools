#!/bin/bash

TRAVIS_BUILD_DIR=$PWD

if [ ! -d tests]; then
    mkdir tests
fi
cd tests
pip install -r requirements.txt

# Install tool dependencies
# =========================
export INSTALL_DIR=/tmp/dep_install && mkdir $INSTALL_DIR
export DOWNLOAD_CACHE=/tmp/download_cache && mkdir $DOWNLOAD_CACHE
for i in $( ls ${TRAVIS_BUILD_DIR}/tools/ )
do 
    planemo dependency_script ${TRAVIS_BUILD_DIR}/tools/$i/
    bash dep_install.sh
    source env.sh
done

# Install Galaxy
# ==============
if [ -d galaxy-master ]; then
    rm -rf galaxy-master
fi
wget https://codeload.github.com/galaxyproject/galaxy/tar.gz/master
tar -zxvf master | tail
rm master
cd galaxy-master

# Configure tools in Galaxy
# =========================
export GALAXY_TEST_UPLOAD_ASYNC=false
export GALAXY_TEST_DB_TEMPLATE=https://github.com/jmchilton/galaxy-downloads/raw/master/db_gx_rev_0127.sqlite

rm -f tool_conf.xml
ln -s ${TRAVIS_BUILD_DIR}/.travis.tool_conf.xml tool_conf.xml
rm -f config/tool_conf.xml.sample
ln -s ${TRAVIS_BUILD_DIR}/.travis.tool_conf.xml config/tool_conf.xml.sample
rm -f config/shed_tool_data_table_conf.xml
ln -s ${TRAVIS_BUILD_DIR}/.travis.tool_data_table_conf.xml config/shed_tool_data_table_conf.xml

for i in $( ls ${TRAVIS_BUILD_DIR}/tools/ )
do 
    ln -s ${TRAVIS_BUILD_DIR}/tools/$i/ tools/$i
    cp ${TRAVIS_BUILD_DIR}/tools/$i/test-data/* test-data/
    if [ -d ${TRAVIS_BUILD_DIR}/tools/$i/tool-data/ ]; then 
        cp ${TRAVIS_BUILD_DIR}/tools/$i/tool-data/* tool-data/
    fi
done

./run.sh --stop-daemon || true
python scripts/fetch_eggs.py

# Test tools
# ==========
python ./scripts/functional_tests.py -v `python tool_list.py Continuous-Integration-Travis`
#!/bin/bash
if [[ $1 != '--functional' && $1 != '--integration' ]]; then
    echo "Unknow test"
    exit
fi


TRAVIS_BUILD_DIR=$PWD
pip install -r requirements.txt

if [ ! -d tests ]; then
    mkdir tests
fi
cd tests


# Install tool dependencies
# =========================
export INSTALL_DIR=/tmp/dep_install
if [ -d $INSTALL_DIR ]; then
    if [[ -z $2 ]]; then
        rm -rf $INSTALL_DIR
        mkdir $INSTALL_DIR
    elif [[ $2 != '--no-reset' ]]; then
        rm -rf $INSTALL_DIR
        mkdir $INSTALL_DIR
    fi
else
    mkdir $INSTALL_DIR
fi


export DOWNLOAD_CACHE=/tmp/download_cache
if [ -d $DOWNLOAD_CACHE ]; then
    if [[ -z $2 ]]; then
        rm -rf $DOWNLOAD_CACHE
        mkdir $DOWNLOAD_CACHE
    elif [[ $2 != '--no-reset' ]]; then
        rm -rf $DOWNLOAD_CACHE
        mkdir $DOWNLOAD_CACHE
    fi
else
    mkdir $DOWNLOAD_CACHE
fi

for i in $( ls ${TRAVIS_BUILD_DIR}/packages/ )
do 
    planemo dependency_script ${TRAVIS_BUILD_DIR}/packages/$i/
    bash dep_install.sh
    source env.sh
done

for i in $( ls ${TRAVIS_BUILD_DIR}/tools/ )
do 
    planemo dependency_script ${TRAVIS_BUILD_DIR}/tools/$i/
    bash dep_install.sh
    source env.sh
done

# Install Galaxy
# ==============
function install_galaxy {
    wget https://codeload.github.com/galaxyproject/galaxy/tar.gz/master
    tar -zxvf master | tail
    rm master
}

if [ -d "galaxy-master" ]; then
    if [[ -z $2 ]]; then
        rm -rf galaxy-master
        install_galaxy
    elif [[ $2 != '--no-reset' ]]; then
        rm -rf galaxy-master
        install_galaxy
    fi
else
    install_galaxy
fi
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


if [ $1 == '--functional' ]; then
    ./run.sh --stop-daemon || true
    python scripts/fetch_eggs.py

    # Test tools
    # ==========
    python ./scripts/functional_tests.py -v `python tool_list.py Continuous-Integration-Travis`
elif [ $1 == '--integration' ]; then
    ./run.sh
else
    echo "Unknow test"
fi
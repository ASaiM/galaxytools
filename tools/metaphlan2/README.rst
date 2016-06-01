Galaxy wrappers for MetaPhlAn2
==============================

Galaxy should be able to automatically install the dependencies, i.e. the
MetaPhlAn2 binaries.

After installation, you must tell Galaxy about the defaut database with
clade-specific marker genes, and where to find it:

* Put the ``metaphlan2_db.loc`` file in the ``tool-data/`` folder, after uncommenting last line
* Download whole MetaPhlan2 source code: https://bitbucket.org/biobakery/metaphlan2/get/2.5.0.zip
* Unzip it
* Move ``db_v20`` folder into ``dependency_dir/metaphlan2/2.5.0/bebatut/package_metaphlan2_2_5_0/...`` folder

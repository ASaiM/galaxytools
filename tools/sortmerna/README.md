Galaxy wrapper for SortMeRNA
============================

SortMeRNA is a tool for RNA filtering based on local sequence alignment against 
rRNA database. For more information, check the [user manual](http://bioinfo.lifl.fr/RNA/sortmerna/code/SortMeRNA-user-manual-v1.7.pdf)

# Installation

## Automated installation

On a Galaxy instance, the wrapper can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tool and data, ...

## Manual installation

For manual installation, the files `sortmerna.xml` must be put in the `tools/sortmerna/`
 folder and add the XML files to Galaxy's `tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="Sort RNA" id="sortmerna">
    <tool file="sortmerna/sortmerna.xml" />
</section>
```

The SortMeRNA database must also be referenced in Galaxy. The `tool-data/sortmerna_rRNA_databases.loc.sample`
must be copy in Galaxy's `tool-data` folder. And Galaxy's `config/tool_data_table_conf.xml.sample`
have to be completed:

```
!-- Locations of public ribosomal databases -->
<table name="sortmerna_rRNA_databases" comment_char="#">
    <columns>value, name, path</columns>
    <file path="tool-data/sortmerna_rRNA_databases.loc" />
</table>
```

SortMeRNA must be installed somewhere on the system path. It can be done using:

```
planemo dependency_script ~/repositories/galaxytools/tools/sortmerna/
bash dep_install.sh
source env.sh
```

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid sortmerna
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff ~/repositories/galaxytools/tools/sortmerna/
```

or:

```
planemo shed_update -t toolshed --check_diff ~/repositories/galaxytools/tools/sortmerna/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details
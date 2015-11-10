Galaxy wrapper for RDPTools
===========================

RDPTols is an open source command-line tool suite for performing a complete 
workflow of analysis tasks of NGS data. For more information, check the 
[Github repository](https://github.com/rdpstaff/RDPTools)

# Installation

## Automated installation

On a Galaxy instance, the wrappers can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tools and data, ...

## Manual installation

For manual installation, the `.xml` files must be put in the `tools/rdptools/`
 folder and add the XML files to Galaxy's `tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="RDPTools" id="rdptools">
    <tool file="rdptools/framebot.xml" />
</section>
```

The database must also be referenced in Galaxy. The files in `tool-data/`
must be copied in Galaxy's `tool-data` folder. And Galaxy's `config/tool_data_table_conf.xml.sample`
have to be completed:

```
!-- Locations of public ribosomal databases -->
<table name="framebot_ref_gene_databases" comment_char="#">
    <columns>value, name, path</columns>
    <file path="tool-data/framebot_ref_gene_databases.loc" />
</table>
```

RDPTools must be installed somewhere on the system path. It can be done using:

```
planemo dependency_script ~/repositories/galaxytools/packages/package_ant_1_9_6/
bash dep_install.sh
source env.sh

planemo dependency_script ~/repositories/galaxytools/tools/rdptools/
bash dep_install.sh
source env.sh
```

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid rdptools
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff ~/repositories/galaxytools/tools/rdptools/
```

or:

```
planemo shed_update -t toolshed --check_diff ~/repositories/galaxytools/tools/rdptools/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details
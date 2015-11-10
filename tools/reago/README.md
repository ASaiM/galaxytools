Galaxy wrapper for Reago
========================

PRINSEQ is an assembly tool for 16S ribosomal RNA recovery from metagenomic data.
For more information, check the 
[Github repository](https://github.com/chengyuan/reago-1.1)

# Installation

## Automated installation

On a Galaxy instance, the wrapper can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tool and data, ...

## Manual installation

For manual installation, the files `reago.xml` and `format_reago_input_files.py` 
must be put in the `tools/reago/` folder and add the XML files to Galaxy's 
`tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="Assemble 16S rRNA" id="reago">
    <tool file="reago/reago.xml" />
</section>
```

PRINSEQ must be installed somewhere on the system path. It can be done using:

```
planemo dependency_script ~/repositories/galaxytools/packages/package_genometools_1_5_7/
bash dep_install.sh
source env.sh

planemo dependency_script ~/repositories/galaxytools/tools/reago/
bash dep_install.sh
source env.sh
```

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid reago
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff ~/repositories/galaxytools/tools/reago/
```

or:

```
planemo shed_update -t toolshed --check_diff ~/repositories/galaxytools/tools/reago/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details
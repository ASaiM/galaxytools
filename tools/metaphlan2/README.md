Galaxy wrapper for MetaPhlAn2
=============================

MetaPhlAn is a computational tool for profiling the composition of microbial 
communities (Bacteria, Archaea, Eukaryotes and Viruses) from metagenomic shotgun 
sequencing data with species level resolution. For more information, check the 
[user manual](https://bitbucket.org/biobakery/metaphlan2)

# Installation

## Automated installation

On a Galaxy instance, the wrapper can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tool and data, ...

## Manual installation

For manual installation, the files `metaphlan2.xml` must be put in the `tools/metaphlan2/`
 folder and add the XML files to Galaxy's `tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="Profile microbial community composition" id="metaphlan2">
    <tool file="metaphlan2/metaphlan2.xml" />
</section>
```

MetaPhlAn2 must be installed somewhere on the system path. 

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid metaphlan2
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff --shed_target ~/repositories/galaxytools/tools/metaphlan2/
```

or:

```
planemo shed_update -t toolshed --check_diff --shed_target ~/repositories/galaxytools/tools/metaphlan2/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details
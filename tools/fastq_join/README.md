Galaxy wrapper for FastQ-Join
=============================

FastQ-Join is a command-line tool to assemble paired-end reads. For more 
information, check the [website](https://code.google.com/p/ea-utils/wiki/FastqJoin)

# Installation

## Automated installation

On a Galaxy instance, the wrapper can be automatically installed using the 
ToolShed. This will automatically install the dependencies, configure the Galaxy
instance for the tool and data, ...

## Manual installation

For manual installation, the files `fastq_join.xml` must be put in the `tools/fastq_join/`
 folder and add the XML files to Galaxy's `tool_conf.xml` (in `config` folder) as 
normal:

```
<section name="Assemble paired-end reads" id="fastq_join">
    <tool file="fastq_join/fastq_join.xml" />
</section>
```

FastQ-Join must be installed somewhere on the system path. It can be done using:

```
planemo dependency_script ~/repositories/galaxytools/tools/fastq_join/
bash dep_install.sh
source env.sh
```

To test the Galaxy integration, the functional tests can be runned:

```
./run_tests.sh -sid fastq_join
```

# Bug Reports

Any bug can be filed in an issue [here](https://github.com/ASaiM/galaxytools/issues).

# Developers

A release can be pushed to the test or main "Galaxy Tool Shed", using the following 
Planemo commands (with required Tool Shed access detailed in `~/.planemo.yml`):

```
planemo shed_update -t testtoolshed --check_diff ~/repositories/galaxytools/tools/fastq_join/
```

or:

```
planemo shed_update -t toolshed --check_diff ~/repositories/galaxytools/tools/fastq_join/
```

# License (Apache 2) 

This wrapper are released under Apache 2 License. See the [LICENSE file](https://github.com/ASaiM/galaxytools/blob/master/LICENSE) for details
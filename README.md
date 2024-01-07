# Clouds-command-line-helper

A set of common command lines to use aws, gcp, azu and oci formatted in jinja2 templates. It is possible to generate linux ou windows like multiline commands.

## Installation 

In the "scopes" directory, you put the files for variables values in yaml format. You should create different files with your own naming convention according to your projects. 

## Usage

To generate cloud command lines, it's just with the short script j2render.py:

./j2rendy.py -s gcp-myproject-variables.yaml -t gcp-vpc-create.j2 -o gcp-myproject-vpc-create.sh 

for example, the gcp-myproject-variables.yaml in the scope directory:
```yaml
variablescopes:
- { VmName: instance-1,
    VmProject: oca-infra-xp-lab,
    VmOsImage: rhel-8,
    VmOsImageProject: rhel-cloud,
    VmMachineType: e2-medium,
    VmZoneLocation: europe-west9-a,
    VmVpcName: lab-test-project,
    VmVpcSubnet: back,
    VmIsPublic: false,
    VmIsShielded: true,
    isCodeisLinux: false
  }
```
## Contributing

You are welcome to add some template files with common command used in order to jumpstart projects or labs quickly.  

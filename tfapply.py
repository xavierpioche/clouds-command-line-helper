import subprocess
import sys
import yaml
import json 
import argparse

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

parser = argparse.ArgumentParser(description="example : -e 1 0 0 -s titi tutu toto", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-e", "--expect", help="exit code expected to move forward", nargs='+')
parser.add_argument("-s", "--script", help="scripts to execute in order", nargs='+')

args = parser.parse_args()

config = vars(args)

count = 0

if len(config['expect']) == len(config['script']):
    for i in range(len(config['script'])):
        batchfile = open(config['script'][i],"r")
        data = batchfile.readlines()
        longdata = ""
        for line in data:
            longdata = longdata + line.strip() 
        longdata = longdata.replace("^","")
        longdata = longdata.replace("\\","")
        print("> executing : " + longdata)
        process = subprocess.Popen(longdata, shell=True, stdout=subprocess.PIPE)
        process.wait()
        print("> retour : " + str(process.returncode))
        print(config['expect'][count])
        if process.returncode != int(config['expect'][count]):
            break
        batchfile.close()
        count+=1
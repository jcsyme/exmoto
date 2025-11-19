#
#  THINGS TO DO ON SETUP
#

#
# set juliapkg path environment variable here to point to julia json
# install julia 
#

import os, os.path
from setuptools import setup



# read in requirements and install
dir_cur = os.path.dirname(os.path.realpath(__file__))
fp_requirements = os.path.join(dir_cur, "requirements.txt")

flag_version = "python_version"

if os.path.isfile(fp_requirements):
    with open(fp_requirements, "r") as fl:
        reqs = fl.readlines()
        
        # get python version
        #py_version = [x.replace(flag_version, "") for x in reqs if flag_version in x]
        #py_version = py_version[0] if (len(py_version) > 0) else None
        reqs = [x for x in reqs if flag_version not in x]


# call setup
setup(
    author = "James Syme",
    author_email = "jsyme@tec.mx",
    description = "EXploratory MOdeling TOolkit",
    include_package_data = True,
    license = "MIT",
    name = "EXMOTO",
    packages = [
        "exmoto.core",
        "exmoto.data_management",
        #"exmoto.manager"
        "exmoto.utilities",
    ],
    package_data = {
        "": [
            "attributes/**",
            "docs/**",
            "ref/**"
        ]
    },
    #python_requires = py_version,
    url = "http://github.com/jcsyme/exmoto",
    version = "1.0.0",
    zip_safe = False
)




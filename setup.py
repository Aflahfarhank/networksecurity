"""
The setup.py file is an essential part of packaging and distributing python projects. 
It is used by setuptools to define the configuration of your project,
 such as its metadata, dependencies, and more
"""

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    reads the requirements.txt file and return a list of dependencies
    """
    requirements_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as f:
            #read lines from the file and strip whitespace and ignore empty lines
            lines=f.readlines()
            for line in lines:
                requirements=line.strip()
                #ignore empty lines and -e .
                if requirements and requirements != "-e .":
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements_lst

print(get_requirements())


setup(
    name="network_security",
    version="0.1.0",
    author="aflah",
    author_email="aflahfarhan9899@gmail.com",
    description="A network security project",
    packages=find_packages(),
    install_requires=get_requirements(),
)
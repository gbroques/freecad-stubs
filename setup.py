import os
import re

from setuptools import find_namespace_packages, setup

packages = find_namespace_packages()

def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return stubs

package_data = {}
for package in packages:
    stubs = find_stubs(package)
    package_data[package] = stubs

with open('environment.yml', 'r') as file:
        content = file.read()
        match = re.search('freecad==([0-9]+?\.[0-9]+?\.[0-9]+?)', content)
        if not match:
            raise ValueError('No freecad version found in environment.yml')
        version = match.group(1)

setup(
    name="freecad-stubs",
    maintainer="G Roques",
    maintainer_email="groques360@gmail.com",
    description="PEP 561 type stubs for freecad",
    url="https://github.com/gbroques/freecad-stubs",
    license="LGPL-2.1-or-later",
    version=version,
    packages=packages,
    package_data=package_data,
    zip_safe=False,
)

from setuptools import setup, find_packages

setup(
    name="DevashishCalculator",
    version="1.0.0",
    description= "Calculator",
    author="Devashish",
    author_email="thyanchor@gmail",
    license="MIT",
    packages=find_packages(exclude=["PackageTest.Test"])
)


# (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest>python -m venv virt //command 1
#
# (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest>cd virt
#
# (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest\virt>cd Scripts
#
# (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest\virt\Scripts>activate //commannd 2
#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest\virt\Scripts>cd ../..
#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest>python setup.py sdist //commannd 3
# running sdist
# running egg_info
# creating DevashishCalculator.egg-info
# writing DevashishCalculator.egg-info\PKG-INFO
# writing dependency_links to DevashishCalculator.egg-info\dependency_links.txt
# writing requirements to DevashishCalculator.egg-info\requires.txt
# writing top-level names to DevashishCalculator.egg-info\top_level.txt
# writing manifest file 'DevashishCalculator.egg-info\SOURCES.txt'
# reading manifest file 'DevashishCalculator.egg-info\SOURCES.txt'
# writing manifest file 'DevashishCalculator.egg-info\SOURCES.txt'
# warning: sdist: standard file not found: should have one of README, README.rst, README.txt, README.md
#
# running check
# warning: check: missing required meta-data: url
#
# creating DevashishCalculator-1.0.0
# creating DevashishCalculator-1.0.0\CalculatorMultipleOperands
# creating DevashishCalculator-1.0.0\DevashishCalculator.egg-info
# creating DevashishCalculator-1.0.0\Test
# copying files to DevashishCalculator-1.0.0...
# copying setup.py -> DevashishCalculator-1.0.0
# copying CalculatorMultipleOperands\CalculateForMultipleOperands.py -> DevashishCalculator-1.0.0\CalculatorMultipleOperands
# copying CalculatorMultipleOperands\__init__.py -> DevashishCalculator-1.0.0\CalculatorMultipleOperands
# copying DevashishCalculator.egg-info\PKG-INFO -> DevashishCalculator-1.0.0\DevashishCalculator.egg-info
# copying DevashishCalculator.egg-info\SOURCES.txt -> DevashishCalculator-1.0.0\DevashishCalculator.egg-info
# copying DevashishCalculator.egg-info\dependency_links.txt -> DevashishCalculator-1.0.0\DevashishCalculator.egg-info
# copying DevashishCalculator.egg-info\requires.txt -> DevashishCalculator-1.0.0\DevashishCalculator.egg-info
# copying DevashishCalculator.egg-info\top_level.txt -> DevashishCalculator-1.0.0\DevashishCalculator.egg-info
# copying Test\TestCalculator2Operands.py -> DevashishCalculator-1.0.0\Test
# copying Test\TestCalculatorMultipleOperands.py -> DevashishCalculator-1.0.0\Test
# copying Test\__init__.py -> DevashishCalculator-1.0.0\Test
# Writing DevashishCalculator-1.0.0\setup.cfg
# Creating tar archive
# removing 'DevashishCalculator-1.0.0' (and everything under it)
#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest>


# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest>cd dist
#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest\dist>pip install DevashishCalculator-1.0.0.tar.gz //commannd 4
# Processing c:\users\dnigam\pycharmprojects\pluralsightpythonintermediate\packagetest\dist\devashishcalculator-1.0.0.tar.gz
# Installing collected packages: DevashishCalculator
#   Running setup.py install for DevashishCalculator ... done
# Successfully installed DevashishCalculator-1.0.0
# You are using pip version 10.0.1, however version 20.1 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.


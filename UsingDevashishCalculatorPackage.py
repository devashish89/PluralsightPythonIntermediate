#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate\PackageTest\dist>cd ../..
#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate>pip install DevashishCalculator-1.0.0.tar.gz
# Processing c:\users\dnigam\pycharmprojects\pluralsightpythonintermediate\devashishcalculator-1.0.0.tar.gz
# Installing collected packages: DevashishCalculator
#   Found existing installation: DevashishCalculator 1.0.0
#     Uninstalling DevashishCalculator-1.0.0:
#       Successfully uninstalled DevashishCalculator-1.0.0
#   Running setup.py install for DevashishCalculator ... done
# Successfully installed DevashishCalculator-1.0.0
# You are using pip version 10.0.1, however version 20.1 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.

#
# (virt) (base) C:\Users\dnigam\PycharmProjects\PluralsightPythonIntermediate>pip show DevashishCalculator
# Name: DevashishCalculator
# Version: 1.0.0
# Summary: Calculator
# Home-page: UNKNOWN
# Author: Devashish
# Author-email: thyanchor@gmail
# License: MIT
# Location: c:\users\dnigam\pycharmprojects\pluralsightpythonintermediate\packagetest\virt\lib\site-packages
# Requires:
# Required-by:
# You are using pip version 10.0.1, however version 20.1 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.



from PackageTest.CalculatorMultipleOperands.CalculateForMultipleOperands import sum, multiply
from PackageTest.Calculator2Operands import sub, division

print(sum(1,2,3,4))
print(multiply(1,2,3,4))

print(sub(4,2))
print(division(2,3))


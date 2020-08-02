import sys
print(sys.float_info)

print(sys.int_info)

####### IMP. ######################
print("0.8-0.7", 0.8-0.7)
### fix for above ############
from decimal import Decimal
print(Decimal(Decimal(0.8)-Decimal(0.7))) ##same problem with float
print(Decimal('0.8')-Decimal('0.7')) ##correct

###### IMP. ###############################
print(Decimal('Infinity'))
print(Decimal('-Infinity'))
print(Decimal('NaN'))

######## IMP.###############
print("'-7 % 3 = -1'",-7 % 3)
print("'-7 % 3 = -1'", Decimal('-7') % Decimal('3'))

print("'-7 // 3 = -2'", -7 //3)
print("'-7 // 3 = -2'", Decimal('-7') // Decimal('3'))

import math
print(math.sqrt(Decimal('.81')))

################# Fractions #################################
from fractions import Fraction
print(Fraction(2,3))
print(Fraction(0.75))
print(Fraction(0.1)) #problem because => 3602879701896397/36028797018963968
print(Fraction(Decimal('0.1')))

print(Fraction('2/3') + Fraction('4/5'))
print(Fraction(2,3)+Fraction(4,5))

print(Fraction('2/3') % Fraction('4/5'))
print(Fraction(2,3) % Fraction(4,5))

print(math.sqrt(Fraction(2,3)))
print(math.sqrt(0.666666666666))


######### Complex Nos. ##################
print(type(3+4j))
print(complex(3,4))
print(complex('3+4j'))

c = -2 -5j
print("real part of complex", c.real)
print("imaginary part of complex", c.imag)
print("conjugate", c.conjugate())

try:
    math.sqrt(-1)
except ValueError as e:
    print(e)

import cmath
print(cmath.sqrt(-1))

phase = cmath.phase(complex(1,1)) #hypotunese
print(phase)

print(abs(complex(1,1)))
print(cmath.polar(complex(1,1)))

absolute , phase = cmath.polar(complex(1,1))
print("abs:{} and phase: {}".format(absolute, phase))


################################################################

def inductance(val):
    return complex(0, +val)

def capacitance(val):
    return complex(0, -val)

def resistance(val):
    return complex(val,0)

def impedance(components):
    z = sum(components)
    return z

z = impedance([inductance(10), capacitance(5), resistance(20)])
print(z)
print(cmath.phase(z), "radians")
print(math.degrees(cmath.phase(z)), "degrees")

####### round()################################

print(round(0.67854, 3))

## IMP.###############
print(round(1.5)) # 2 rounding is towards even no for .5 values
print(round(2.5)) # 2 rounding towards even no. for .5 values
print(round(2.6)) #3
print(round(2.4)) #2

print("issue it should be 2.68:", round(2.675,2))
print("issue fix:", round(Decimal('2.675'),2))
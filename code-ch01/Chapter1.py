# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper

from ecc import FieldElement
# -

from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)
print(a == a)

# ### Exercise 1
#
# Write the corresponding method `__ne__` which checks if two `FieldElement` objects are _not equal_ to each other.
#
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_ne`

# +
# Exercise 1

reload(ecc)
run(ecc.FieldElementTest("test_ne"))
# -

print(7 % 3)

print(-27 % 13)

# ### Exercise 2
#
# Solve these problems in \\(F_{57}\\) (assume all +'s here are \\(+_{f}\\) and -`s here \\(-_{f}\\))
#
# * 44+33
# * 9-29
# * 17+42+49
# * 52-30-38

# +
# Exercise 2

# remember that % is the modulo operator
prime = 57
# 44+33
print((44+37) % prime)
# 9-29
print((9-29) % prime)
# 17+42+49
print((17+42+49) % prime)
# 52-30-38
print((52-30-38) % prime)
# -

from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a+b==c)

# ### Exercise 3
#
# Write the corresponding `__sub__` method which defines the subtraction of two `FieldElement` objects.
#
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_sub`

# +
# Exercise 3

reload(ecc)
run(ecc.FieldElementTest("test_sub"))
# -

# ### Exercise 4
#
# Solve the following equations in \\(F_{97}\\) (again, assume ⋅ and exponentiation are field versions):
#
# * 95⋅45⋅31
# * 17⋅13⋅19⋅44
# * \\(12^{7}\\)⋅\\(77^{49}\\)

# +
# Exercise 4

prime = 97

# 95*45*31
print((95*45*31)%prime)
# 17*13*19*44
print((17*13*19*44)%prime)
# 12**7*77**49
print((12**7*77**49)%prime)
# -

# ### Exercise 5
#
# For k = 1, 3, 7, 13, 18, what is this set in \\(F_{19}\\)?
#
# {k⋅0, k⋅1, k⋅2, k⋅3, ... k⋅18}
#
# Do you notice anything about these sets?

# +
# Exercise 5

prime = 19
k = 1  # 3, 7, 13 and 18 are the other possibilities
# loop through all possible k's 0 up to prime-1
# calculate k*iterator % prime
for k in (1,3,7,13,18):
    print([k*i % prime for i in range(prime)])
# Hint - sort!
for k in (1,3,7,13,18):
    print(sorted([k*i % prime for i in range(prime)]))
# -

from ecc import FieldElement
a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a*b==c)

# ### Exercise 6
#
# Write the corresponding `__mul__` method which defines the multiplication of two Finite Field elements.
#
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_mul`

# +
# Exercise 6

reload(ecc)
run(ecc.FieldElementTest("test_mul"))
# -

from ecc import FieldElement
a = FieldElement(3, 13)
b = FieldElement(1, 13)
print(a**3==b)

# ### Exercise 7
#
# For p = 7, 11, 17, 31, what is this set in \\(F_{p}\\)?
#
# {\\(1^{(p-1)}\\), \\(2^{(p-1)}\\), \\(3^{(p-1)}\\), \\(4^{(p-1)}\\), ... \\((p-1)^{(p-1)}\\)}

# +
# Exercise 7

primes = [7, 11, 17, 31, 43]
for p in primes:
    print([pow(k, p-1, p) for k in range(1, p)])
# -

# ### Exercise 8
#
# Solve the following equations in \\(F_{31}\\):
#
# * 3 / 24
# * \\(17^{-3}\\)
# * \\(4^{-4}\\)⋅11

# +
# Exercise 8

p = 31
# 3/24
print(3 * pow(24, p-2, p) % p)
# 17**-3
print(pow(17, p-4, p))
# 4**-4*11
print((pow(4, p-5, p) * 11) % p)
# -

# ### Exercise 9
#
# Write the corresponding `__truediv__` method which defines the division of two field elements.
#
# Note that in Python3, division is separated into `__truediv__` and `__floordiv__`. The first does normal division, the second does integer division.
#
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_div`

# +
# Exercise 9

reload(ecc)
run(ecc.FieldElementTest("test_div"))
# -

from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a**-3==b)



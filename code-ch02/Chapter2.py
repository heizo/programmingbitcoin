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

from ecc import Point
# -

from ecc import Point
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, -2, 5, 7)


# ### Exercise 1
#
# Determine which of these points are on the curve \\(y^{2}\\)=\\(x^{3}\\)+5x+7:
#
# (2,4), (-1,-1), (18,77), (5,7)

# +
# Exercise 1

# (2,4), (-1,-1), (18,77), (5,7)
# equation in python is: y**2 == x**3 + 5*x + 7
def on_curve(x, y):
    return y**2 == x**3 + 5*x + 7
print(on_curve(2,4))
print(on_curve(-1,-1))
print(on_curve(18,77))
print(on_curve(5,7))
# -

# ### Exercise 2
#
# Write the `__ne__` method for `Point`.
#
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_ne`

# +
# Exercise 2

reload(ecc)
run(ecc.PointTest("test_ne"))
# -

from ecc import Point
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(None, None, 5, 7)
print(p1 + inf)
print(inf + p2)
print(p1 + p2)

# ### Exercise 3
#
# Handle the case where the two points are additive inverses. That is, they have the same `x`, but a different `y`, causing a vertical line. This should return the point at infinity.
#
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_add0`

# +
# Exercise 3

reload(ecc)
run(ecc.PointTest("test_add0"))
# -

# ### Exercise 4
#
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+5x+7, what is (2,5) + (-1,-1)?

# +
# Exercise 4

from ecc import Point

a = 5
b = 7
x1, y1 = 2, 5
x2, y2 = -1, -1

# (x1,y1) + (x2,y2)
s = (y2 - y1) / (x2 - x1)
x3 = s**2 - x1 - x2
y3 = s * (x1 - x3) - y1
print(x3, y3)
# -

# ### Exercise 5
#
# Write the `__add__` method where \\(x_{1}\\)≠\\(x_{2}\\)
#
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_add1`

# +
# Exercise 5

reload(ecc)
run(ecc.PointTest("test_add1"))
# -

# ### Exercise 6
#
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+5x+7, what is (-1,-1) + (-1,-1)?

# +
# Exercise 6

from ecc import Point

a = 5
b = 7
x1, y1 = -1, -1
# (-1,-1) + (-1,-1)
s = (3 * x1**2 + a) / (2 * y1)
x3 = s**2 - 2*x1
y3 = s*(x1-x3)-y1
print(x3,y3)
# -

# ### Exercise 7
#
# Write the `__add__` method when \\(P_{1}\\)=\\(P_{2}\\).
#
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_add2`

# +
# Exercise 7

reload(ecc)
run(ecc.PointTest("test_add2"))
# -



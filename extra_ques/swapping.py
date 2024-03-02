# Created on Wed Jan 03 2024
#
# Author: Prakul Sharma
#
# Question # swap 2 numbers using only 2 variables
#
#
# Thoughts:
# using division and multiplication
#
#

a = 10
b = 5

print(f'a is {a} and b is {b}')

# a, b = b, a

a = a + b
b = a - b
a = a - b

print(f'a is {a} and b is {b}')
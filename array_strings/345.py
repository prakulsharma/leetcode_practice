#
# Created on Wed Dec 27 2023
#
# Author: Prakul Sharma
#
# Question #345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Thoughts:
#
#
#

s = "hello"
s = list(s)
# output is "holle"
indx = []
values = []
for i,x in enumerate(s):
    if x in list('aeiouAEIOU'):
        indx.append(i)
        values.append(x)

values = values[::-1]
for j in range(len(indx)):
    s[indx[j]] = values[j]

print(''.join(s))
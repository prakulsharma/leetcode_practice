#
# Created on Tue Dec 19 2023
#
# Author: Prakul Sharma
#
# Question #1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# 
# Thoughts:
# I am going to start with the shorter string of the two. let's say 2 strings are ABCABCABC and ABCABC
# Now, I start with ABCABC which is str2 and check if length of strings are divisible with remainder 0
# then checking if mutliplying str2 with that integer gives me str1
# I keep on slicing out the last letter and repeat 2nd step

str1 = "ABCDEF"
str2 = "ABC"

if len(str1) < len(str2):
    base = str1
elif len(str1) > len(str2):
    base = str2
else:
    base = str1

for i in range(len(base)):
    if len(str1)%len(base) == 0  and len(str1)%len(base) == 0:
        if base * int(len(str1)/len(base)) == str1 and base * int(len(str2)/len(base)) == str2:
            output = base
            break
        else:
            output = ""
        base = base[:-1]
    else:
        base = base[:-1]
        output = ""

print(output)
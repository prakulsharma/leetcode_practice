#
# Created on Tue Dec 19 2023
#
# Author: Prakul Sharma
#
# Question #1768. Merge Strings Alternately
#
# Thoughts:
# I can do it using simple built-in for loop inside join
#
#
word1 = "abc"
word2 = "pqrst"

if len(word1) != len(word2):
    if len(word1) > len(word2):
        suffix = word1[len(word2):]
    else:
        suffix = word2[len(word1):]
else:
    suffix = ""

print("".join(["".join(i) for i in list(zip(word1, word2))]) + suffix)

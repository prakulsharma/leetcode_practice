# Created on Thu Dec 28 2023
#
# Author: Prakul Sharma
#
# Question #443. String Compression
# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
#
# Thoughts:
#
#
#

chars = ["a","a","b","b","c","c","c"]

s = []
temp = ''
count = 1
for c in chars:
    if c == temp:
        count += 1
    else:
        if count > 1:
            s.append(str(count))
        s.append(c) 
        count = 1
        temp = c 
if count > 1:
    s.append(str(count))
chars[:] = list(''.join(s)) # The line chars = list(''.join(s)) doesn't modify the original chars list passed as the argument. Instead, it creates a new list and assigns it to the local variable chars. To modify the original list, you should use chars[:] = list(''.join(s)) or a similar approach.
output_len = len(chars)
print(output_len)

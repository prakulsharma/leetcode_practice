# Created on Fri Dec 29 2023
#
# Author: Prakul Sharma
#
# Question #283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#
# Thoughts:
#
#

nums = [0,0,1]

print('array is:', nums)

position = 0
for num in nums:
    if num != 0:
        nums[position] = num
        position += 1

for i in range(position, len(nums)):
    nums[i] = 0

print('array is:', nums)
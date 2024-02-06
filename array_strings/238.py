#
# Created on Thu Dec 28 2023
#
# Author: Prakul Sharma
#
# Question #238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Thoughts:
#
#
#
import numpy as np
nums = [1,2,3,4]
length = len(nums)
answer = [1] * length

left_product = 1
for i in range(1, length):
    left_product *= nums[i - 1]
    answer[i] = left_product

right_product = 1
for i in range(length - 2, -1, -1):
    right_product *= nums[i + 1]
    answer[i] *= right_product

print(answer)
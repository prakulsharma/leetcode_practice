#
# Created on Thu Dec 28 2023
#
# Author: Prakul Sharma
#
# Question #334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
# 
# Thoughts:
#
import numpy as np
nums = [1,2,3,4,5]

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
s = Solution()
print(s.increasingTriplet(nums))
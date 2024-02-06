# Created on Sun Jan 07 2024
#
# Author: Prakul Sharma
#
# Question #446. Arithmetic Slices II - Subsequence
#
# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# The test cases are generated so that the answer fits in 32-bit integer.
# 
# Thoughts: getting all the possible combinations of subsequences would be a bad idea for sure.
#
# 

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:

        return len(nums)
        
    #     generate_subsequences(my_array, 0, [], result_subsequences)

    # def createSequence(self, nums: list[int]) -> List[int]:
    #     if index == len(arr):
    #         result.append(current_subsequence)
    #         return

    #     generate_subsequences(arr, index + 1, current_subsequence + [arr[index]], result)
    #     generate_subsequences(arr, index + 1, current_subsequence, result)
        
    # def isSequence(self, sequence: List[int]) -> bool:
    #     diff = sequence[0] - sequence[1]

    #     for i in range(1, len(sequence) - 1):
    #         if sequence[i] - sequence[i+1] != diff:
    #             return False
    #     return True
    

input = [2,4,6,8,10]
s = Solution()
output = s.numberOfArithmeticSlices(nums=input)
print(output)
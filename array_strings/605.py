#
# Created on Mon Dec 25 2023
#
# Author: Prakul Sharma
#
# Question #605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n
# new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# 
# Thoughts:
# Sliding window to check sum = 1 for 2 adjacent values. (count of sum not equal to 1)/2 should be equal to n
#
import numpy as np

flowerbed = [0]
n = 1

sum = 0
new_arr = ''.join([str(i) for i in flowerbed]).split('1')
print('new_arr', new_arr)

if len(new_arr) <= 1:
    if new_arr == ['0']:
        sum += 1
        print('sum', sum)
    else:
        sum += np.ceil(len(new_arr[0])/2)
        print('sum', sum)
else:
    if new_arr[0]:
        sum += len(new_arr[0])//2
        print('sum', sum)
    if new_arr[-1]:
        sum += len(new_arr[-1])//2
        print('sum', sum)
new_arr = new_arr[1:-1]
print('middle array', new_arr)
new_arr = [(len(i) - 1) // 2 if (len(i) - 1) >= 0 else 0 for i in new_arr]
print('middle array sum', np.sum(new_arr))
print('start and end array sum', sum)
print('total sum', int(np.sum(new_arr) + sum))

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n == 0:
#             return True
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n == 0:
#                     return True
#         return False
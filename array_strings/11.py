# Created on Sun Jan 07 2024
#
# Author: Prakul Sharma
#
# Question #11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
#
# Thoughts:
# Brute force - make every possible container
#
#

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # brute force
        # area = -1
        # for i in range(len(height) - 1):
        #     for j in range(i+1, len(height)):
        #         # print(f'left line: {height[i]}, right line: {height[j]}, base len: {j-i}, max height: {min(height[i], height[j])}')
        #         if (j-i) * min(height[i], height[j]) > area:
        #             area = (j-i) * min(height[i], height[j])
        # return area

        # optimized
        left = 0
        right = len(height) - 1
        area = (right - left) * min(height[left], height[right])

        while left != right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            if (right - left) * min(height[left], height[right]) > area:
                area = (right - left) * min(height[left], height[right])

        return area
    
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
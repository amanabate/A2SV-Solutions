# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =  len(nums)
        output = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                output[stack.pop()] = nums[i]

            stack.append(i)
        
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                output[stack.pop()] = nums[i]
        
        return output

        
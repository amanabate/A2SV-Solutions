# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num

            stack.append(num)


        for num in stack:
            next_greater[num] = -1

        result = []

        for num in nums1:
            result.append(next_greater[num])
            
        return result

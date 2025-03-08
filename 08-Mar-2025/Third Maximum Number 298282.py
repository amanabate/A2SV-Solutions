# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        unique_element = list(set(nums))
        unique_element.sort()
        
        if len(unique_element) >= 3:
            return unique_element[-3]
        else:
            return unique_element[-1]
# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        distinct_element = list(set(nums))
        distinct_element.sort()
        
        if len(distinct_element) >= 3:
            return distinct_element[-3]
        else:
            return distinct_element[-1]


            

        
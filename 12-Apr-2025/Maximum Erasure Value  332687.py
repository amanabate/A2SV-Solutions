# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        start = 0
        max_sum = 0
        current_sum = 0
        num_map = {}
        
        for end in range(len(nums)):
            num = nums[end]
                  
            if num in num_map and num_map[num] >= start:
                while start <= num_map[num]:
                    current_sum -= nums[start]
                    start += 1
            
            current_sum += num
            num_map[num] = end
        
            max_sum = max(max_sum, current_sum)
        
        return max_sum

            
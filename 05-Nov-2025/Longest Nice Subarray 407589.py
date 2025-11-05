# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        current_or = 0
        max_len = 0
        
        for right in range(len(nums)):
            while current_or & nums[right] != 0:
                current_or ^= nums[left]  
                left += 1
            
            # Add nums[right] to current_or
            current_or |= nums[right]
            
            # Update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len
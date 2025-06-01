# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = nums[0]
        total = 0

        for num in nums:
            if total < 0:
                total = 0

            total += num
            result = max(result, total)
        
        return result
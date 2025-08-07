# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if (target + total) % 2 == 1 or abs(target) > total:
            return 0

        subset_sum = (target + total) // 2

        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  

        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[subset_sum]
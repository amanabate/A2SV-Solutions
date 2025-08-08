# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        memo = {}

        def lis(i):
            if i in memo:
                return memo[i]

            max_len = 1  
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    max_len = max(max_len, 1 + lis(j))

            memo[i] = max_len
            return max_len

        return max(lis(i) for i in range(n))
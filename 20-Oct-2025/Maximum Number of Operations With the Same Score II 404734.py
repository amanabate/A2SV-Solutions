# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}  # (i, j, score) -> result

        def dfs(i, j, score):
            if j - i + 1 < 2:
                return 0

            if (i, j, score) in memo:
                return memo[(i, j, score)]

            res = 0
            if i + 1 <= j and nums[i] + nums[i + 1] == score:
                res = max(res, 1 + dfs(i + 2, j, score))
            if j - 1 >= i and nums[j] + nums[j - 1] == score:
                res = max(res, 1 + dfs(i, j - 2, score))
            if nums[i] + nums[j] == score:
                res = max(res, 1 + dfs(i + 1, j - 1, score))

            memo[(i, j, score)] = res
            return res

        return max(
            dfs(0, n - 1, nums[0] + nums[1]),
            dfs(0, n - 1, nums[-1] + nums[-2]),
            dfs(0, n - 1, nums[0] + nums[-1])
        )

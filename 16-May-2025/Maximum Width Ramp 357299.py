# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
  
        candidates = []
        n = len(nums)

        for idx in range(n):
            if not candidates or nums[idx] < nums[candidates[-1]]:
                candidates.append(idx)

        result = 0

        for end in range(n - 1, -1, -1):
            while candidates and nums[end] >= nums[candidates[-1]]:
                start = candidates.pop()
                result = max(result, end - start)

        return result

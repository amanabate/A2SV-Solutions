# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/


class Solution:
    def getMaximumConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        old_interval = [0, 0]

        for num in nums:
            new_interval = [old_interval[0] + num, old_interval[1] + num]

            if new_interval[0] - old_interval[1] <=  1:
                start = min(old_interval[0], new_interval[0])
                end = max(old_interval[1], new_interval[1])
                old_interval = [start, end]
            else:
                break

        return old_interval[1] - old_interval[0] + 1
# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums = set(nums)  
        long_length = -1

        for num in nums:
            length = 1

            while num * num in nums:
                num *= num
                length += 1

            if length > 1:
                long_length = max(long_length, length)

        return long_length

        
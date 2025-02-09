# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        half = len(nums) // 2
        for key, value in count.items():
            if value > half:
                return key
        
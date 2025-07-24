# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        operations = 0
        n = len(nums)
        prev = nums[-1] 

        for i in range(n - 2, -1, -1):

            if nums[i] <= prev:
                prev = nums[i]
            else:
                parts = (nums[i] + prev - 1) // prev  
                operations += parts - 1
                prev = nums[i] // parts  

        return operations

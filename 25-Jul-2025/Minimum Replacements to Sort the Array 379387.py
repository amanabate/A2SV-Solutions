# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        #  [7, 15, 4, 5]
                   nw pv
        new_value = nums[index]
        prev_value = nums[index + 1]
        curr_opt = new_value // prev_value + some  ceiling opt
        prev_value = new_value // curr_opt

        """

        N = len(nums)
        total_opt = 0
        prev_value = nums[-1]

        for index in range(N - 2, -1, -1):
            new_value = nums[index]
            
            if new_value <= prev_value:
                prev_value = nums[index]
                continue
            curr_opt =ceil( new_value /prev_value) 
            prev_value = new_value // curr_opt
            
           
            
            total_opt += curr_opt - 1
        return total_opt

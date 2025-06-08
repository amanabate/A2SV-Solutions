# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        val_to_index = {}

        for i, val in enumerate(nums):
            val_to_index[val] = i

        for old_val, new_val in operations:
            index = val_to_index.pop(old_val)
            nums[index] = new_val
            val_to_index[new_val] = index
        
        return nums
# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        dict_nums = Counter(nums)
        result = []
        for key, value in dict_nums.items():
            if value >= 2:
                result.append(key)
                
        return result
                
        
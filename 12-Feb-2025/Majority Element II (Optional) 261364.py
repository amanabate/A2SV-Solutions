# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        dict_nums = Counter(nums)
        output = []
    
        for key, value in dict_nums.items():
            if value > n // 3:
                output.append(key)
        return output

        
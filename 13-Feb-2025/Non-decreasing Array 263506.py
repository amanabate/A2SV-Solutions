# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:  
                count += 1
                
                if count > 1:
                    return False
                
                if i - 2 >= 0 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        
        return True

        
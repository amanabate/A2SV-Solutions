# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == val:
                nums[i], nums[right] = nums[right], nums[i]  
                right -= 1  
            else:
                i += 1  

        return right + 1
            
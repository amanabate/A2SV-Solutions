# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        stk1 = []
        stk2 = []
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i + 1] = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                stk1.append(nums[i])
            elif nums[i] == 0:
                stk2.append(nums[i])

        return stk1 + stk2

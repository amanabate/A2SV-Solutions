# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = len(nums)
        nums_arr = [1] * k
        pref = 1

        for i in range(k):
            nums_arr[i] = pref
            pref *= nums[i]

            suff = 1
        for i in range(k - 1, -1, -1):
            nums_arr[i] *= suff
            suff *= nums[i]

        return nums_arr
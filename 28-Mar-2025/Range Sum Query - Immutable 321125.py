# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.pref = []
        i = 0
        for j in nums:
            i += j
            self.pref.append(i)  

    def sumRange(self, left, right):
 
        Right_sum = self.pref[right]

        if left > 0:
            Left_sum = self.pref[left - 1]
        else:
            Left_sum = 0
        return Right_sum - Left_sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
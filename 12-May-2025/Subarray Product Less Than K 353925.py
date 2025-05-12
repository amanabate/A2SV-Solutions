# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1: 
           return 0

        product = 1
        count = 0
        start = 0

        for end in range(len(nums)):
            product *= nums[end]

            while product >= k and start <= end:
                product //= nums[start]
                start += 1

            
            count += (end - start + 1)

        return count
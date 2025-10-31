# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

from math import gcd

class Solution:
    def subarrayLCM(self, nums, k):
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        n = len(nums)
        count = 0
        
        for i in range(n):
            curr_lcm = 1
            for j in range(i, n):
                # if nums[j] does not divide k, break early
                if k % nums[j] != 0:
                    break
                
                curr_lcm = lcm(curr_lcm, nums[j])
                
                if curr_lcm == k:
                    count += 1
                elif curr_lcm > k:
                    break
        
        return count

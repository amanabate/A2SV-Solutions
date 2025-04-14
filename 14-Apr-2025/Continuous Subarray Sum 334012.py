# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder_map = {0: -1}  
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder in remainder_map:
                prev_index = remainder_map[remainder]
                if i - prev_index >= 2:
                    return True
            else:
                remainder_map[remainder] = i  
                
        return False

            
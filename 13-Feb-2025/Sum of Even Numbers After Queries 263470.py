# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
            even_sum = 0
            for num in nums:
                if num % 2 == 0:
                    even_sum += num
            
            result = []
            
            for val, index in queries:
                old_value = nums[index]
                nums[index] += val
                
                if old_value % 2 == 0:
                    even_sum -= old_value  
                
                if nums[index] % 2 == 0:
                    even_sum += nums[index]  
                
                result.append(even_sum)
            
            return result

        
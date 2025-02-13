# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
            visited = set()  
            duplicates = []  
            
            for num in nums:
                if num in visited:
                    duplicates.append(num)
                else:
                    visited.add(num)
            
            return duplicates
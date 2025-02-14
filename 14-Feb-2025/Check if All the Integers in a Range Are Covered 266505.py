# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            
            covered = False
            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break  
       
            if not covered:
                return False

        return True
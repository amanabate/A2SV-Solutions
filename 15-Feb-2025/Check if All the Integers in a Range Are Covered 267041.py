# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:


        lst = []
        for start, end in ranges:
            for num in range(start, end + 1):
                lst.append(num)
        
        for num in range(left, right + 1):
            if num not in lst:
                return False
        return True

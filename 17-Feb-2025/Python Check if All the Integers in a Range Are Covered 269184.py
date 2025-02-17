# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        List = []
        for start, end in ranges:
            for num in range(start, end + 1):
                List.append(num)
        
        for num in range(left, right + 1):
            if num not in List:
                return False
        return True

# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        freq = {}
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])
                freq[num] = 0 

    
        remaining = sorted(freq.keys())
        for num in remaining:
            if freq[num] > 0:  
                result.extend([num] * freq[num])

        return result
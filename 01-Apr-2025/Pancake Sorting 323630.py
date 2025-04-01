# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flips = []
        n = len(arr)
        
        for i in range(n, 1, -1):
            max_index = arr.index(max(arr[:i]))
            
            if max_index == i - 1:
                continue  
            
            if max_index != 0:
                flips.append(max_index + 1)
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            
           
            flips.append(i)
            arr[:i] = arr[:i][::-1]
        
        return flips
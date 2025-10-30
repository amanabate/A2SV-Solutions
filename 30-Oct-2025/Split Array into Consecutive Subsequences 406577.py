# Problem: Split Array into Consecutive Subsequences - https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import Counter
        
        freq = Counter(nums)
        need = Counter()
        
        for x in nums:
            if freq[x] == 0:
                continue
            
            if need[x] > 0:
                need[x] -= 1
                need[x + 1] += 1
                freq[x] -= 1
            
            elif freq[x] > 0 and freq[x + 1] > 0 and freq[x + 2] > 0:
                freq[x] -= 1
                freq[x + 1] -= 1
                freq[x + 2] -= 1
                need[x + 3] += 1
            
            else:
                return False
        
        return True

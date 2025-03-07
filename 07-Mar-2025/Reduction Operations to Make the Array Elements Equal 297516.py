# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        freq = Counter(nums)  
        sorted_keys = sorted(freq.keys(), reverse=True)  
        operations = 0
        count = 0  

        for num in sorted_keys[:-1]:
            count += freq[num]  
            operations += count 

        return operations



# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        conc = ''
        for num in b:
            conc += str(num)

        return pow(a, int(conc), 1337)


       


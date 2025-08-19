# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        bit_pos = 0
        while num > 0:
            # If the current bit is 0, set it to 1 in the result
            if (num & 1) == 0:
                res |= (1 << bit_pos)
            num >>= 1
            bit_pos += 1
        return res
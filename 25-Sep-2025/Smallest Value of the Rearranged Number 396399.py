# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        if num > 0:
            digits = sorted(str(num))  # ascending
            # find first non-zero digit
            for i, d in enumerate(digits):
                if d != '0':
                    # put that digit in front
                    smallest = [digits[i]] + digits[:i] + digits[i+1:]
                    break
            return int("".join(smallest))
        else:
            digits = sorted(str(-num), reverse=True)  # descending
            return -int("".join(digits))
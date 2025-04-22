# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = list(s)
        i = 0
        while i < len(s_list):
            if s_list[i].isdigit():
                if i > 0:  
                    s_list.pop(i - 1)  
                    i -= 1  
                s_list.pop(i)  
            else:
              i += 1
        return ''.join(s_list)
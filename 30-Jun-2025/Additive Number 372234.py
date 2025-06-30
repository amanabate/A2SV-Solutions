# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):  # end of first number
            for j in range(i + 1, n):  # end of second number
                num1, num2 = num[:i], num[i:j]
                
                # Skip if numbers have leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                while j < n:
                    sum_str = str(int(num1) + int(num2))
                    if not num.startswith(sum_str, j):
                        break
                    j += len(sum_str)
                    num1, num2 = num2, sum_str
                
                if j == n:
                    return True
        
        return False
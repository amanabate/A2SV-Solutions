# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        lst = [num for num in range(int(math.sqrt(c)) + 1)]  
        
        right = len(lst) - 1
        left = 0

        while right >= left:
            sum_square = lst[right] * lst[right] + lst[left] * lst[left] 

            if sum_square == c:
                return True
            elif sum_square < c:
                left += 1
            else:
                right -= 1

        return False

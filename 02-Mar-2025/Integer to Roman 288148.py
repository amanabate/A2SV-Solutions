# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        
        Symbol_Value = [
                    (1000, "M"), 
                    (900, "CM"), 
                    (500, "D"), 
                    (400, "CD"),
                    (100, "C"), 
                    (90, "XC"), 
                    (50, "L"), 
                    (40, "XL"),
                    (10, "X"), 
                    (9, "IX"), 
                    (5, "V"), 
                    (4, "IV"), 
                    (1, "I")
                            
                        ]

        result = ""
    
        for value, symbol in Symbol_Value:
            while num >= value:
                result += symbol
                num -= value
            
        return result
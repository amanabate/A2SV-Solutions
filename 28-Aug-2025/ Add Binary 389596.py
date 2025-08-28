# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        num_a = int(a, 2)
        num_b = int(b, 2)

        total = num_a + num_b

        binary_result = bin(total)

        return binary_result[2:]
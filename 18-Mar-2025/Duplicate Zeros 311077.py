# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        output = []

        for num in arr:
            if num == 0:
                output.append(0)
                output.append(0)
                if len(output) == len(arr):
                    break
            elif num != 0:
                output.append(num)
                if len(output) == len(arr):
                    break

        for i in range(len(arr)):
            arr[i] = output[i]

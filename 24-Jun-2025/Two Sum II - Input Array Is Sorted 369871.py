# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            Sum = numbers[left] + numbers[right]

            if Sum == target:
                return [left + 1, right + 1]

            elif Sum > target:
                right -= 1
            else:
                left += 1


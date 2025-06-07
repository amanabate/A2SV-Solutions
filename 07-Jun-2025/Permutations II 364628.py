# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        counter = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1

                    backtrack(path)

                    path.pop()
                    counter[num] += 1

        backtrack([])
        return res
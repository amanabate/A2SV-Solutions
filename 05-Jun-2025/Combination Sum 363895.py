# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(start, curr_comb, curr_sum):
            
            if curr_sum <= target:
                if curr_sum == target:
                    answer.append(curr_comb[:])

                    return
            else:
                return


            for i in range(start, len(candidates)):
                curr_comb.append(candidates[i])

                backtrack(i, curr_comb, curr_sum + candidates[i])  
                # Not i+1 because we can reuse
                
                curr_comb.pop()

        backtrack(0, [], 0)
        return answer
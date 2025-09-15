# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[n] = 0 base case
        
        for i in range(n - 1, -1, -1):  # process from last to first
            points, brain = questions[i]
            next_q = i + brain + 1
            take = points + (dp[next_q] if next_q < n else 0)
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        
        return dp[0]
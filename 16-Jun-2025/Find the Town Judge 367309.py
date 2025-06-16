# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score = [0] * (n + 1)

        for a, b in trust:
            trust_score[a] -= 1  
            trust_score[b] += 1 

        for person in range(1, n + 1):
            if trust_score[person] == n - 1:
                return person

        return -1
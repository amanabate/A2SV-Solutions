# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total_skill = skill[0] + skill[-1]
        chemistry = 0

        for i in range(n // 2):
            if skill[i] + skill[-1 - i] != total_skill:
                return -1
            chemistry += skill[i] * skill[-1 - i]
        
        return chemistry
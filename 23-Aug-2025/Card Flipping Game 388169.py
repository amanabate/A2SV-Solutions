# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution:
    def flipgame(self, fronts, backs):
        banned = set()  # Numbers that appear on both sides of the same card
        n = len(fronts)
        
        for i in range(n):
            if fronts[i] == backs[i]:
                banned.add(fronts[i])
        
        candidates = set(fronts + backs) - banned
        
        if not candidates:
            return 0
        
        return min(candidates)
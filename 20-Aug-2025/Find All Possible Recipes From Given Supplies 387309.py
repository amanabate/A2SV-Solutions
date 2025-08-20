# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {}
        
        # initialize indegree for recipes
        for r, ing in zip(recipes, ingredients):
            indegree[r] = len(ing)
            for item in ing:
                graph[item].append(r)
        
        q = deque(supplies)
        made = []
        
        while q:
            item = q.popleft()
            for r in graph[item]:
                indegree[r] -= 1
                if indegree[r] == 0:
                    made.append(r)
                    q.append(r)
        
        return made
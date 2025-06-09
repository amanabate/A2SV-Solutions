# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        ans = [float('inf')]  
        children = [0] * k

        def backtrack(i):
            if i == n:
                ans[0] = min(ans[0], max(children))
                return
            for j in range(k):
                children[j] += cookies[i]

                if max(children) < ans[0]:
                    backtrack(i + 1)

                children[j] -= cookies[i]

                if children[j] == 0:
                    break

        backtrack(0)
        
        return ans[0]

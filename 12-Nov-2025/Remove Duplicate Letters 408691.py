# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter

        counter = Counter(s)  
        stack = []
        seen = set()  

        for char in s:
            # Decrease remaining count
            counter[char] -= 1

            # Skip if character is already in stack
            if char in seen:
                continue

    
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return ''.join(stack)
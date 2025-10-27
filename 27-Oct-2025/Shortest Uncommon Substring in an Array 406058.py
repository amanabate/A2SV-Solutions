# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:

        substring_count = defaultdict(set)

        # Step 1: Record which strings contain each substring
        for i, word in enumerate(arr):
            seen = set()
            for l in range(len(word)):
                for r in range(l + 1, len(word) + 1):
                    sub = word[l:r]
                    if sub not in seen:
                        substring_count[sub].add(i)
                        seen.add(sub)

        # Step 2: Build answer list
        answer = []
        for i, word in enumerate(arr):
            unique_subs = []
            for l in range(len(word)):
                for r in range(l + 1, len(word) + 1):
                    sub = word[l:r]
                    if len(substring_count[sub]) == 1:
                        unique_subs.append(sub)
            
            if not unique_subs:
                answer.append("")
            else:
                # Sort by shortest length, then lexicographically smallest
                unique_subs.sort(key=lambda x: (len(x), x))
                answer.append(unique_subs[0])

        return answer
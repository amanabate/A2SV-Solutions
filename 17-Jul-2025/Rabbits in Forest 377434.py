# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)
        for a in answers:
            freq[a] += 1

        total = 0
        for k in freq:
            group_size = k + 1
            group_count = math.ceil(freq[k] / group_size)
            total += group_count * group_size

        return total

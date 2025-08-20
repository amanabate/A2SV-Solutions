# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # make max-heap by pushing negatives
        heap = [-p for p in piles]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            reduced = largest - largest // 2
            heapq.heappush(heap, -reduced)

        return -sum(heap)
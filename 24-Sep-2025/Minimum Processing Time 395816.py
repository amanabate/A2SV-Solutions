# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        ans = 0
        for i in range(len(processorTime)):
            # pick 4 tasks for processor i
            max_task = tasks[i * 4]  # largest among the 4 (since sorted desc)
            ans = max(ans, processorTime[i] + max_task)

        return ans
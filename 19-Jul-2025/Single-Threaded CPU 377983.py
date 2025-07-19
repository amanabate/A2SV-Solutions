# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #  (enque, processingTime, index)
        arr = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]

        arr.sort()

        time_tracker = 0
        ans = []
        min_heap = []
        i = 0
        n = len(tasks)

        for _ in range(n):
            # push all tasks available at current time
            while i < n and arr[i][0] <= time_tracker:
                heappush(min_heap, (arr[i][1], arr[i][2]))
                i += 1

            # our cpu is empty but the arrival time is in the future
            if not min_heap and i < n:
                time_tracker = arr[i][0]
                heappush(min_heap, (arr[i][1], arr[i][2]))
                i += 1

            # min_heap should store the process untill the process in the cpu finish
            # (pro_time, index)
            if min_heap:
                pr, ind = heappop(min_heap)
                time_tracker += pr
                ans.append(ind)

        return ans

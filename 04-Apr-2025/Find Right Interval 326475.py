# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        n = len(intervals)
        arr = []
        for i in range(n):
            s = intervals[i][0]
            e = intervals[i][1]
            arr.append((s, e, i))

        arr.sort()

        starts = []
        for i in range(n):
            starts.append(arr[i][0])

        res = []
        for i in range(n):
            res.append(-1)

        for i in range(n):
            end = intervals[i][1]
            l = 0
            r = n - 1
            while l <= r:
                m = (l + r) // 2
                if starts[m] >= end:
                    r = m - 1
                else:
                    l = m + 1
            if l < n:
                res[i] = arr[l][2]

        return res
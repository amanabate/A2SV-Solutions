# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canFinish(boxes, shipLimit, allowedDays):
            total = 0
            daysNeeded = 1

            for weight in boxes:
                if total + weight > shipLimit:
                    daysNeeded += 1
                    total = 0
                total += weight
            
            return daysNeeded <= allowedDays

        minCapacity = max(weights)
        maxCapacity = sum(weights)

        while minCapacity < maxCapacity:

            testCapacity = (minCapacity + maxCapacity) // 2

            if canFinish(weights, testCapacity, days):
                maxCapacity = testCapacity
                
            else:
                minCapacity = testCapacity + 1

        return minCapacity

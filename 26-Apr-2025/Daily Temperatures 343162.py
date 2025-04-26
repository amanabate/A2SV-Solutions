# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0] * len(temperatures)

        for current_day in range(len(temperatures)):
            while stack and temperatures[current_day] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                output[previous_day] = current_day - previous_day
            stack.append(current_day)
            
        return output
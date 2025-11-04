# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts):
        max_w = 0
        for cust in accounts:
            s = 0
            for money in cust:
                s += money
            if s > max_w:
                max_w = s
        return max_w
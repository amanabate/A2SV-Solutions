# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        def fib_rec(n):
            if n <= 1:
               return n
            return fib_rec(n - 1) + fib_rec(n - 2)
            
        return fib_rec(n)
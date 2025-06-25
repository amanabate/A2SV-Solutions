# Problem: B - Too Hot to Code! - https://codeforces.com/gym/617023/problem/B

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    max_len = 1
    current_len = 1

    for i in range(1, n):
        if a[i] - a[i-1] <= k:
            current_len += 1
            max_len = max(max_len, current_len)

        else:
            current_len = 1
            
    print(n - max_len)
# Problem: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min((a + b) // 4, min(a, b)))

# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())

for r in range(n):
    if r % 2 == 0:
        print("#" * m)  
    elif r % 4 == 1:
        print("." * (m - 1) + "#")  
    else:
        print("#" + "." * (m - 1))  

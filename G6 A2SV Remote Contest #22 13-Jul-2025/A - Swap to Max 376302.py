# Problem: A - Swap to Max - https://codeforces.com/gym/622136/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    last_a = []
    last_b = []

    for i in range(n):
        if a[i] > b[i]:
            last_a.append(b[i])
            last_b.append(a[i])
        else:
            last_a.append(a[i])
            last_b.append(b[i])
    
    print(max(last_a) * max(last_b))
# Problem: B - Ski Resort - https://codeforces.com/gym/603156/problem/B

t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    length = 0

    for temp in a + [q + 1]:  
        if temp <= q:
            length += 1
        else:
            if length >= k:
                num = length - k + 1
                count += num * (num + 1) // 2 
            length = 0  

    print(count)

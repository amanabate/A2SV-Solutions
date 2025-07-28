# Problem: B - Planning Journey - https://codeforces.com/gym/625306/problem/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    i = 0
    journeys = 0
    current_clear = 0

    while i < n:
        if a[i] == 0:
            current_clear += 1
            if current_clear == k:
                journeys += 1
                current_clear = 0
                i += 1  # skip rest day
        else:
            current_clear = 0
        i += 1

    print(journeys)

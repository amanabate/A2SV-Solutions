# Problem: A - Card Game - https://codeforces.com/gym/616066/problem/A

t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    a = list(map(int, input().split()))  # First player's cards
    b = list(map(int, input().split()))  # Second player's cards

    if max(a) > max(b):
        print("YES")
    else:
        print("NO")

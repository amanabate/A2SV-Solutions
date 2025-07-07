# Problem: A - Twice - https://codeforces.com/gym/619446/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1

    score = 0
    for count in freq.values():
        
        while count >= 2:
            score += 1
            count -= 2

    print(score)

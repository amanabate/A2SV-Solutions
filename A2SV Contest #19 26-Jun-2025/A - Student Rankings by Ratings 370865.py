# Problem: A - Student Rankings by Ratings - https://codeforces.com/gym/617023/problem/A

n = int(input())

rates = list(map(int, input().split()))

positions = []

for i in range(n):
    current_rate = rates[i]

    count = 0

    for r in rates:
        if r > current_rate:
            count += 1

    position = count + 1

    positions.append(position)

print(' '.join(map(str,positions)))
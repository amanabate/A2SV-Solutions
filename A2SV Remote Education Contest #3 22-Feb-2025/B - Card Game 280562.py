# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

n = int(input())
cards = list(map(int, input().split()))

cards_list = []

for i in range(n):
    pair = (cards[i], i + 1)
    cards_list.append(pair)

cards_list.sort()

for i in range(n // 2):
    smallest = cards_list[i][1]
    largest = cards_list[n - i - 1][1]
    print(smallest, largest)

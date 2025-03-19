# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

n, k = map(int, input().split())

speed = list(map(int, input().split()))

speed.sort(reverse = True)

print(speed[k - 1])
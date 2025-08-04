# Problem: B - Make Product Equal One - https://codeforces.com/gym/626626/problem/B

n = int(input())
a = list(map(int, input().split()))

cost = 0 
neg = 0
zero = 0

for num in a:
    if num > 1:
        cost += num - 1
    elif num < -1:
        cost += abs(num + 1)
        neg += 1
    elif num == 0:
        cost += 1
        zero += 1
    else:
        if num == -1:
            neg += 1
if neg % 2 == 1 and zero == 0:
    cost += 2

print(cost)
# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

n , x = map(int, input().split())
a = [0] * 1006

for _ in range(n):
    left, right = map(int,input().split())
    if left > right:
        left, right = right, left
   
    a[left] += 1
    a[right + 1] -= 1

temp = 0
answer = 1001

for i in range(1001):
    temp += a[i]
    if temp == n:
        answer = min(answer, abs(i - x))

print(answer if answer != 1001 else - 1)

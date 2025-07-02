# Problem: B - New Year Transportation - https://codeforces.com/gym/618729/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))

curr_pos = 1
while curr_pos < t:
    curr_pos += a[curr_pos - 1]

if curr_pos == t:
    print("YES")
else:
    print("NO")
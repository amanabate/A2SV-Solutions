# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if a[j] - a[i] == j - i:
#                 count += 1
#     print(count)


n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))

    count = 0
    mydic = {}

    for i in range(size):
        key = arr[i] - i
        mydic[key] = mydic.get(key, 0) + 1

    for val in mydic.values():
        count += val * (val - 1) // 2
        
    print(count)

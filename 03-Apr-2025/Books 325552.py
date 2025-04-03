# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
books = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + books[i]

def binary_search(prefix, start, target):
    left = start
    right = n
    best = start
    while left <= right:
        mid = (left + right) // 2
        if prefix[mid] - prefix[start] <= target:
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    return best

max_books = 0
for i in range(n):
    j = binary_search(prefix, i, t)
    max_books = max(max_books, j - i)

print(max_books)
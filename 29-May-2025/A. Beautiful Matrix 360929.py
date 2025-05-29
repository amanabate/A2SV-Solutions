# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A


matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
    if 1 in row:
        one_row = i + 1      
        one_col = row.index(1) + 1

moves = abs(one_row - 3) + abs(one_col - 3)
print(moves)

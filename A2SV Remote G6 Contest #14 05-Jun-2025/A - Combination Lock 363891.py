# Problem: A - Combination Lock - https://codeforces.com/gym/610550/problem/A

n = int(input())
original_state = input()
target = input()


dict = {}

for i in range(10):
    for j in range(10):
        forward = abs(i - j)
        backward = 10 - forward
        dict[(i, j)] = min(forward, backward)


moves = 0
for i in range(n):
    from_digit = int(original_state[i])
    to_digit = int(target[i])
    moves += dict[(from_digit, to_digit)]

print(moves)

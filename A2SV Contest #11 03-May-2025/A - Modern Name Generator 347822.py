# Problem: A - Modern Name Generator - https://codeforces.com/gym/605795/problem/A

t = int(input())

for _ in range(t):
    user_input = list(input().split())

    result = []

    for word in user_input:
        result.append(word[0])
    print(''.join(result))



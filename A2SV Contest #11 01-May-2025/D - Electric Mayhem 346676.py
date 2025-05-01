# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

user_input = input().strip()

stack = []

for char in user_input:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
    
if not stack:
    print('Yes')
else:
    print('No')

# Problem: B - Aaron and Repeated Letters - https://codeforces.com/gym/605795/problem/B

user_input = str(input())

stack = []

for ch in user_input:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)
print(''.join(stack))
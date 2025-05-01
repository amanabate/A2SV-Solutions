# Problem: C - Mr. Boomsy - https://codeforces.com/gym/605795/problem/C

t = int(input())

for _ in range(t):
    user_input = str(input())

    stack = []

    for ch in user_input:
        if stack and ch == 'B':
              stack.pop()
        else:
           stack.append(ch)

    print(len(stack))
    

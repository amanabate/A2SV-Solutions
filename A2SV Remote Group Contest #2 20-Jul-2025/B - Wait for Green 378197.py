# Problem: B - Wait for Green - https://codeforces.com/gym/623571/problem/B

t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    
    if c == 'g':
        print(0)
        continue
    
    wait_times = []
    
    green_pos = [i for i in range(n) if s[i] == 'g']
    
    max_wait = 0
    for i in range(n):
        if s[i] == c:
           
            for g in green_pos:
                if g >= i:
                    wait = g - i
                    break
            else:
                wait = (green_pos[0] + n) - i
            max_wait = max(max_wait, wait)
    
    print(max_wait)

# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

t = int(input())  

for _ in range(t):
    n = int(input())  
    s = input() 
    
    first_b = -1  
    last_b = -1   
    

    for i in range(n):
        if s[i] == 'B':
            first_b = i
            break
    
    for i in range(n-1, -1, -1):
        if s[i] == 'B':
            last_b = i
            break
    
    print(last_b - first_b + 1)
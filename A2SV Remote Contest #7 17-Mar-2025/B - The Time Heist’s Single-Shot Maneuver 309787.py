# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B

test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    b = list(map(int, input().split()))
    b1 = b[0]  
    
    
    prev = -float('inf')
    possible = True
    
    for i in range(n):
        choice1 = a[i]
        choice2 = b1 - a[i]
        
       
        if choice1 >= prev and choice2 >= prev:
            chosen = min(choice1, choice2)

        elif choice1 >= prev:
            chosen = choice1

        elif choice2 >= prev:
            chosen = choice2

        else:
            possible = False
            break
        
        prev = chosen
    
    print("YES" if possible else "NO")
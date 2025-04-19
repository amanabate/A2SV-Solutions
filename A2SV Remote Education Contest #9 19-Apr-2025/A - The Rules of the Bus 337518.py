# Problem: A - The Rules of the Bus - https://codeforces.com/gym/603156/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = set()
    
    if n == 1:
        print("YES")
        continue
    
    occupied.add(a[0])
    for i in range(1, n):
        current_seat = a[i]
        left = current_seat - 1
        right = current_seat + 1
        
        if (left not in occupied) and (right not in occupied):
            print("NO")
            break
        occupied.add(current_seat)
    else:
        print("YES")
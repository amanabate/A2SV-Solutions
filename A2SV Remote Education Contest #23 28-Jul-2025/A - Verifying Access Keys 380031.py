# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    
    first_letter_index = n

    for i in range(n):
        if s[i].isalpha():
            first_letter_index = i
            break

    
    digits = s[:first_letter_index]
    letters = s[first_letter_index:]

   
    if digits == ''.join(sorted(digits)) and letters == ''.join(sorted(letters)):
        print("YES")
    else:
        print("NO")

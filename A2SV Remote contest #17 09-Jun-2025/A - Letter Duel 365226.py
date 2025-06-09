# Problem: A - Letter Duel - https://codeforces.com/gym/614464/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    start, end = -1, -1
   
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            start, end = i + 1, i + 2
            break

    if start != -1:
        print(start, end)
    else:
        count_a = s.count('a')
        count_b = s.count('b')

        if count_a == count_b and n >= 2:
            print(1, n)
        else:
            print(-1, -1)


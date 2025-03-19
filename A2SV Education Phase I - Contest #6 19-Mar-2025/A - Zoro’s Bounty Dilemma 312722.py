# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

no_test = int(input())

cases = [input().strip() for i in range(no_test)]

for s in cases:
    if '<' in s and '>' in s:
        print('?')
    elif '<' in s:
        print('<')
    elif '>' in s:
        print('>')
    else:
        print('=')
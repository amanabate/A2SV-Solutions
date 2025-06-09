# Problem: C - Number Mutation - https://codeforces.com/gym/614464/problem/C

a, b = map(int, input().split())

def find_path(a, b):

    path = []
    current = b
    path.append(current)

    while current > a:
        if current % 2 == 0:
            current = current // 2
            path.append(current)
            
        elif current % 10 == 1:
            current = current // 10
            path.append(current)
        else:
            return 
    if current == a:
        path.reverse()
        return path
    else:
        return 

path = find_path(a, b)
if path:
    print("YES")
    print(len(path))
    print(' '.join(map(str, path)))
else:
    print("NO")
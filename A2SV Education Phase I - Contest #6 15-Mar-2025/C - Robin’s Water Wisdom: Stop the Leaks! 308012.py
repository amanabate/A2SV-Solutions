# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

n, A, B = map(int, input().split())
sizes = list(map(int, input().split()))

S = sum(sizes)

first_hole = (sizes[0] * A) / S

if first_hole >= B:
    print(0)

else:

    other_holes = sorted(sizes[1:], reverse = True)

    blocks = 0

    for hole in other_holes:
        S -= hole
        first_hole = (sizes[0] * A) / S
        blocks += 1
        

        if first_hole >= B:
            print(blocks)
            break
    

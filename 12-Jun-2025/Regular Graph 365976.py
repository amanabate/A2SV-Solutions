# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

no_vert, no_edge = map(int, input().split())
degrees = [0] * (no_vert + 1)

for _ in range(no_edge):
    edge1, edge2 = map(int, input().split())
    degrees[edge1] += 1
    degrees[edge2] += 1

if len(set(degrees[1:])) == 1: #If there is only 1 unique value, all degrees are equal 
    print("YES")
else:
    print("NO")
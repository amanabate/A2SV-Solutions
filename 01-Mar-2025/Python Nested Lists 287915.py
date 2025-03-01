# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

n = int(input()) 
students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])


students.sort(key=lambda x: x[1])


lowest = students[0][1]
second_lowest = None

for name, grade in students:
    if grade > lowest:
        second_lowest = grade
        break

names = [name for name, grade in students if grade == second_lowest]


for name in sorted(names):
    print(name)

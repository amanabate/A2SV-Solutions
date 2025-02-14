# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
     
    lst = [] 

    for _ in range(N):
        command = input().split()  
        operation = command[0] 

        if operation == "insert":
            lst.insert(int(command[1]), int(command[2])) 
        elif operation == "print":
            print(lst)  
        elif operation == "remove":
            lst.remove(int(command[1])) 
        elif operation == "append":
            lst.append(int(command[1]))  
        elif operation == "sort":
            lst.sort()  
        elif operation == "pop":
            lst.pop()  
        elif operation == "reverse":
            lst.reverse()  

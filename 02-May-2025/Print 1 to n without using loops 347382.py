# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def  printNos(n, current=1):
    if current > n:
        return
    print(current, end=' ')
    printNos(n, current + 1)


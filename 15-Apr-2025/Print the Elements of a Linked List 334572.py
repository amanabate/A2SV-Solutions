# Problem: Print the Elements of a Linked List - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):

    current = head
    while current:
        print(current.data)
        current = current.next
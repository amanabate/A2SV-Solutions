# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        current = dummy

        while current and current.next:
            if current.next.val == val:
                temp = current.next          
                current.next = temp.next     
            else:
                current = current.next      

        return dummy.next
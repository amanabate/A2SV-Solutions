# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
           return head


        if head.next is None:
            return head


        if k == 0:
            return head

        
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head

      
        k = k % length

        if k == 0:
            tail.next = None
            return head

        fast = head

        for _ in range(k):
            fast = fast.next

        slow = head

        while fast.next != head:
            slow = slow.next
            fast = fast.next

        
        new_head = slow.next

        slow.next = None

        return new_head
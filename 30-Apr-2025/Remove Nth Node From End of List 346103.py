# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = follow = head  

        for _ in range(n):
            lead = lead.next

        if not lead:
            return head.next

        current = head
        while lead.next:
            lead = lead.next
            current = current.next

        current.next = current.next.next
        return head
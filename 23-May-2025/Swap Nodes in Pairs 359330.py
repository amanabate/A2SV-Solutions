# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next

        prev = None
        current = head

        while current and current.next:
            first = current
            second = current.next

         
            first.next = second.next
            second.next = first

           
            if prev:
                prev.next = second

            prev = first
            current = first.next

        return new_head
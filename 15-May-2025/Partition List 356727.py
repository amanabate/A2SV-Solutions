# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_head = less_tail = None
        greater_head = greater_tail = None

        while head:
            next_node = head.next
            head.next = None 
            if head.val < x:
                if not less_head:
                    less_head = less_tail = head
                else:
                    less_tail.next = head
                    less_tail = head
            else:
                if not greater_head:
                    greater_head = greater_tail = head
                else:
                    greater_tail.next = head
                    greater_tail = head

            head = next_node

        if not less_head:
            return greater_head 

        less_tail.next = greater_head  

        return less_head
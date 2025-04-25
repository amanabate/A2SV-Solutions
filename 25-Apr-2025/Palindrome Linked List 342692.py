# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        vals = []
        current = head

        while current:
            vals.append(current.val)
            current = current.next

    
        left, right = 0, len(vals) - 1
        
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1

        return True
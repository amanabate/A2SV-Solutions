# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        

        if not root:
            return 0
        
        total = 0
        queue = deque()
        
        queue.append((root, None, None))
        
        while queue:
            node, parent, grandparent = queue.popleft()
            
            if grandparent and grandparent.val % 2 == 0:
                total += node.val
            
            if node.left:
                queue.append((node.left, node, parent))

            if node.right:
                queue.append((node.right, node, parent))
                
        
        return total
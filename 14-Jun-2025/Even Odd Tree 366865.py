# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def isEvenOddTree(root):
            if not root:
                return True

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()
                val = node.val

                if level % 2 == 0:
                    if val % 2 == 0 or (prev is not None and val <= prev):
                        return False
               
                else:
                    if val % 2 != 0 or (prev is not None and val >= prev):
                        return False

                prev = val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True
# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        return left_same and right_same
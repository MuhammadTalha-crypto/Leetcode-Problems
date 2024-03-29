# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum_ = 0
        
        def inorder(root):
            # result = 0
            if root:
                if root.val > low:
                    inorder(root.left)
                if low <= root.val <= high:
                    self.sum_ +=root.val
                if root.val < high:
                    inorder(root.right)
            # return result
        inorder(root)
        return self.sum_
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lsval = []
        def search(node):
            if node:
                search(node.left)
                lsval.append(node.val)
                search(node.right)
        search(root)
        return lsval[k-1]
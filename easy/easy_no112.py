# https://leetcode.com/problems/path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root: return False
        
        self.res = False
        def myfunc(node,tt):
            if node:
                tt+=node.val
                if node.left==node.right==None: 
                    if (tt==sum): self.res=True
                else:
                    myfunc(node.left, tt)
                    myfunc(node.right, tt)
                
        
        myfunc(root, 0)
        return self.res

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def checksum(node, total):
            if node:
                if node.left==None and node.right==None:
                    return (total+node.val)==sum
                else:
                    return checksum(node.left, total+node.val) or checksum(node.right, total+node.val)
        return checksum(root,0)
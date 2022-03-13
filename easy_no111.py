# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        self.depth = float('inf')
        def myfunc(node,d):
            if node:
                d+=1
                left = myfunc(node.left, d)
                right = myfunc(node.right, d)
                if (left==None) & (right==None): 
                    select = d
                elif (left==None) & (right!=None):
                    select = right
                elif (left!=None) & (right==None):
                    select = left
                else:
                    select = min(left, right)
                self.depth = min(self.depth, select)
                return select
            
        
        myfunc(root, 0)
        return self.depth

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return (left+right+1) if left == 0 or right == 0 else min(left, right)+1
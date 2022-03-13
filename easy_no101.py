# https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def isSymmetric(self, root):
        if not root: return True
        elif (root.left==None) & (root.right==None): return True
        elif (root.left==None) | (root.right==None): return False
        
        self.part = []
        def myfunc(node):
            if node:
                self.part.append(node.val)
                myfunc(node.left)
                myfunc(node.right)
            else:
                self.part.append(None)
                
        myfunc(root.left)
        leftpart = self.part
        
        self.part = []
        def myfunc(node):
            if node:
                self.part.append(node.val)
                myfunc(node.right)
                myfunc(node.left)
            else:
                self.part.append(None)
                
        myfunc(root.right)
        rightpart = self.part
        # print(leftpart, rightpart)
        
        if leftpart==rightpart: return True
        else: return False


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isReversed(root.left, root.right)
        
    def isReversed(self, p, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isReversed(p.left, q.right) and self.isReversed(p.right, q.left)
        elif not p and not q:
            return True
        else:
            return False

# wide 
test_cases = [
    [1,2,2,3,4,4,3],
    [1,2,2,None,3,None,3],
    [1,2,2,2,None,2],
    [1,2,2,3,None,None,3],
    [5,4,1,None,1,None,4,2,None,2,None],
]

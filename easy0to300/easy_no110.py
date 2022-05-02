# https://leetcode.com/problems/balanced-binary-tree/

class Solution1:
    def isBalanced(self):
        self.res=True
        def myfunc(node, d):
            if node:
                left = myfunc(node.left, d+1)
                right = myfunc(node.right, d+1)
                if abs(left-right)>1: self.res = False
                return max(left, right)
            else:
                return d
                
        myfunc(root, 0)
        return self.res

class Solution2:
    def isBalanced(self):
        if not root: return True
        self.gloab = True
        def depth(node):
            if node:
                left = depth(node.left)
                right = depth(node.right)
                if self.gloab:
                    self.gloab = abs(left-right)<=1
                return max(left,right)+1
            else:
                return 0
        depth(root)
        return self.gloab
test_cases = [
    
]
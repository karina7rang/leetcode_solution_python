# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution1:
    def maxDepth(self):
        self.depth = 0
        def myfunc(d, node):
            if node:
                select = max(myfunc(d+1,node.left), myfunc(d+1, node.right))
                self.depth = max(self.depth, select)
                return select
            else:
                return d
        
        myfunc(0, root)
        return self.depth

class Solution2:
    def maxDepth(self):
        def depth(node):
            if node:
                return 1 + max(depth(node.left), depth(node.right))
            else:
                return 0
        
        return depth(root)

test_cases = [
    [3,9,20,null,null,15,7],
    [1,null,2],
    [],
    [1,null,2,3,4],
]
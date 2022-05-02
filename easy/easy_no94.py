# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def inorderTraversal(self, head):
        res = []
        def myfunc(node):
            if node:
                myfunc(node.left)
                res.append(node.val)
                myfunc(node.right)
        myfunc(head)
        return res

class Solution2:
    def inorderTraversal(self, head):
        self.output = []
        
        def visit(node):
            if node:
                visit(node.left)
                self.output = self.output + [node.val]
                visit(node.right)
        visit(head)
        return self.output

test_cases = [
    [1,None,2,3],
    [],
    [1],
    [1,2,3,4,5,6,7],
]

def build_tree(ls):
    def myfunc(vals):
        if vals:
            cur = TreeNode(vals.pop(0))
            cur.left = myfunc(vals)
            cur.right = myfunc(vals)
            return cur
        else:
            return None
    return myfunc(ls)


for i in range(len(test_cases)):
    test_cases[i] = build_tree(test_cases[i])

def print_tree(tree):
    print('------tree-------')
    res = []
    def myfunc(node):
        if node:
            res.append(node.val)
            myfunc(node.left)
            myfunc(node.right)
    myfunc(tree)
    print(res)



for i in test_cases:
    res = Solution1().inorderTraversal(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().inorderTraversal(i)
    print(res)
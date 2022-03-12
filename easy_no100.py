# https://leetcode.com/problems/same-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n)
class Solution1:
    def isSameTree(self,p,q):
        lsp = []
        lsq = []
        def gothrough(node,ls):
            if node:
                ls.append(node.val)
                gothrough(node.left,ls)
                gothrough(node.right,ls)
        gothrough(p,lsp)
        gothrough(q,lsq)
        return lsp==lsq

# O(n)
class Solution2:
    def isSameTree(self,p,q):
        
        def gothrough(node1,node2):
            if node1 and node2:
                if node1.val==node2.val:
                    return (
                        gothrough(node1.left, node2.left)
                        and gothrough(node1.right, node2.right)
                        )
                else:
                    return False
            elif node1 or node2:
                return False
            else:
                return True
        return gothrough(p,q)


class Solution3:
    def isSameTree(self,p,q):
        def myfunc(node1, node2):
            # print(node1, node2)
            if (node1!=None) & (node2!=None):
                if node1.val!=node2.val: 
                    return False
                else:
                    if (myfunc(node1.left, node2.left)) & (myfunc(node1.right, node2.right)):
                        return True
                    else:
                        return False
            elif (node1==None) & (node2==None):
                return True
            else:
                return False
        
        return myfunc(p,q)
test_cases = [
    [[1,2,3],[1,2,3]],
    [[1,2],[1,None,2]],
    [[],[1]],
    [[1],[2]],

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
    test_cases[i] = [build_tree(test_cases[i][0]),build_tree(test_cases[i][1])]


for i,j in test_cases:
    res = Solution1().isSameTree(i,j)
    print(res)
print('------------------')
for i,j in test_cases:
    res = Solution2().isSameTree(i,j)
    print(res)
print('------------------')
for i,j in test_cases:
    res = Solution3().isSameTree(i,j)
    print(res)
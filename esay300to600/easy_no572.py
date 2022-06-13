# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(node1, node2):
            if node1 and node2:
                return node1.val==node2.val and compare(node1.left, node2.left) and compare(node1.right, node2.right)
            elif not node1 and not node2:
                return True
            else:
                return False

        def findstart(node):
            if node:
                if compare(node, subRoot):
                    return True
                else:
                    return findstart(node.left) or findstart(node.right)
            else:
                return False

         
        return findstart(root)



class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if self.compare(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False        
        
    def compare(self, node1, node2):
        if node1 and node2:
            return node1.val==node2.val and self.compare(node1.left, node2.left) and self.compare(node1.right, node2.right)
        elif not node1 and not node2:
            return True
        else:
            return False
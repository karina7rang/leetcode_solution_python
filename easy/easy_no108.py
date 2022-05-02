# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution1:
    def sortedArrayToBST(self):
        def myfunc(lsnum, node=None):
            if lsnum:
                mid = len(lsnum)//2
                node = TreeNode(lsnum[mid])
                
                node.left = myfunc(lsnum[:mid], node.left)
                node.right = myfunc(lsnum[mid+1:], node.right)
                return node

        if not nums: return None
        else:
            return myfunc(nums)

class Solution2:
    def sortedArrayToBST(self):
        if not nums:
            return None
        head = TreeNode(nums[len(nums)//2])
        head.left = self.sortedArrayToBST(nums[:len(nums)//2])
        head.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        return head

test_cases = [
    [-10,-3,0,5,9],
    [1,3],
    [0,1,2,3,4,5,6],
    [],
]

# run
for i in test_cases:
    res = Solution1().sortedArrayToBST(i)
    print(res)
print('------------------')
for i in test_cases:
    res = Solution2().sortedArrayToBST(i)
    print(res)
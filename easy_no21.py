# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        
        def myfunc(node, input1, input2):
            if not input1: node.next = input2
            elif not input2: node.next = input1
            else:
                if input1.val<=input2.val:
                    node.next = ListNode(input1.val)
                    myfunc(node.next, input1.next, input2)
                else:
                    node.next = ListNode(input2.val)
                    myfunc(node.next, input1, input2.next)
                

        myfunc(res, l1,l2)
        return res.next

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)

        def addnode(node, input1, input2):
            if not input1:
                node.next = input2
            elif not input2:
                node.next = input1
            else:
                if input1.val<=input2.val:
                    node.next = ListNode(input1.val)
                    addnode(node.next, input1.next, input2)
                else:
                    node.next = ListNode(input2.val)
                    addnode(node.next, input1, input2.next)

        addnode(res, l1, l2)
        return res.next





test_cases = [
    [[1,2,4],[1,3,4]],
    [[1,5],[2,3,4]],
    # [[],[]],
    # [[],[0]],
]

def build_link(ls):
    if ls:
        reslink = None
        for i in ls[::-1]:
            tmpnode = ListNode(i)
            tmpnode.next = reslink
            reslink = tmpnode
        return reslink
    else:
        return ListNode(None)

for i in range(len(test_cases)):
    l1 = test_cases[i][0]
    l2 = test_cases[i][1]
    test_cases[i] = [build_link(l1), build_link(l2)]

def print_node(node):
    print('------start-------')
    cur = node
    while cur:
        print(cur.val)
        cur = cur.next





for i,j in test_cases:
    res = Solution1().mergeTwoLists(i,j)
    print_node(res)
print('------------------')
for i,j in test_cases:
    res = Solution2().mergeTwoLists(i,j)
    print_node(res)
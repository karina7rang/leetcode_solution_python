# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def deleteDuplicates(self, head):
        if not head: return head
        def rmv(node):
            if node.next:
                if node.val==node.next.val:
                    if node.next.next:
                        node.next = node.next.next
                        node = rmv(node)
                    else:
                        node.next = None
                else:
                    node.next = rmv(node.next)
            return node
        return rmv(head)

class Solution2:
    def deleteDuplicates(self, head):
        self.res = ListNode(None)
        self.curr = None
        def keepdisct(cures, node):
            if node:
                if node.val!=self.curr:
                    self.curr=node.val
                    cures.next=ListNode(node.val)
                    keepdisct(cures.next, node.next)
                else:
                    keepdisct(cures, node.next)
                    
        keepdisct(self.res, head)
        return self.res.next

class Solution3:
    def deleteDuplicates(self, head):
        if not head: return head

        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

test_cases = [
    [],
    [1],
    [1,1,2],
    [1,1,1,3],
    [1,1,1,1,4],
    [1,1,2,3,3],
    [1,2,2,2,4],
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
    test_cases[i] = build_link(test_cases[i])

def print_node(node):
    print('------node-------')
    cur = node
    while cur:
        print(cur.val)
        cur = cur.next


# for i in test_cases:
#     res = Solution1().deleteDuplicates(i)
#     print_node(res)
# print('------------------')
# for i in test_cases:
#     res = Solution2().deleteDuplicates(i)
#     print_node(res)
print('------------------')
for i in test_cases:
    res = Solution3().deleteDuplicates(i)
    print_node(res)
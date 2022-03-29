# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def myfunc(node):
            if node:
                res = myfunc(node.next)
                cur = ListNode(node.val)
                res.next = cur # None, 2
                return res.next
            else:
                return self.output
        
        self.output = ListNode(None)
        myfunc(head)
        return self.output.next
                
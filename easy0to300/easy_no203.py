# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(None)
        res.next = head
        def myfunc(node):
            if node and node.next:
                if node.next.val==val:
                    node.next = node.next.next
                    myfunc(node)
                else:
                    myfunc(node.next)
        myfunc(res)
        return res.next



class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(None)
        res.next = head
        cur = res
        while cur.next:
            if cur.next.val==val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(None)
        res.next = head
        cur = res
        while cur and cur.next:
            if cur.next.val==val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next
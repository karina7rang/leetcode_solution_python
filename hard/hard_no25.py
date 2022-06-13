# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head

        left = right = head
        flag = True
        res = jump = ListNode(None)
        while flag:
            loopk=0
            while right and loopk<k:
                right = right.next
                loopk+=1
            if loopk==k:
                rev = right
                pointer = left
                for _ in range(k):
                    rev, rev.next, pointer = pointer, rev, pointer.next
                jump.next, jump, left = rev, left, right
            else:
                flag=False
        return res.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointer = head
        for _ in range(k):
            if not pointer:
                return head
            else:
                pointer = pointer.next
        
        rev = None
        pointer = head
        for _ in range(k):
            rev, rev.next, pointer = pointer, rev, pointer.next
        
        head.next = self.reverseKGroup(pointer, k)
        return rev
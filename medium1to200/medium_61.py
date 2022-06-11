# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def explorenode(node):
            if node.next.next == None:
                newhead = node.next
                node.next = None
                return newhead
            else:
                return explorenode(node.next)
        
        if not head or not head.next:
            return head
        
        for i in range(k):
            newhead = explorenode(head)
            newhead.next = head
            head = newhead
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        newhead = head
        n  = 1
        while newhead.next:
            newhead = newhead.next
            n+=1
        
        if k%n==0:
            return head
        else:
            y = n-k%n
            
        def myfunc(node, x):
            if x>0:
                return myfunc(node.next, x-1)
            else:
                newhead = node.next
                node.next = None
                return newhead
        newhead = myfunc(head, y-1)
        
        def myfunc(node):
            if node.next:
                myfunc(node.next)
            else:
                node.next = head
        myfunc(newhead)
        return newhead
        
                
        
        
        
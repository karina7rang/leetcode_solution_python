# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return ls==ls[::-1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = {}
        length = 0
        while head:
            if head.val in ls:
                ls[head.val].append(length)
            else:
                ls[head.val] = [length]
            length+=1    
            head = head.next
        length-=1
        for i,j in ls.items():
            if sum(j)!=((len(j)/2)*length):
                return False
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val==slow.val:
            rev = rev.next
            slow = slow.next

        return not rev
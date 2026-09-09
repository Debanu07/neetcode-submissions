# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode()
        c=0
        curr=d
        while l1 and l2:
            total=l1.val+l2.val+c
            digits=total%10
            c=total//10
            curr.next=ListNode(digits)
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1:
            total=l1.val+c
            digits=total%10
            c=total//10
            curr.next=ListNode(digits)
            curr=curr.next
            l1=l1.next
        while l2:
            total=l2.val+c
            digits=total%10
            c=total//10
            curr.next=ListNode(digits)
            curr=curr.next
            l2=l2.next
        if c:
            curr.next=ListNode(c)
        return d.next
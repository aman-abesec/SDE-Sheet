#======================================================
#      2. Add Two Numbers
#      https://leetcode.com/problems/add-two-numbers/
#      https://youtu.be/LBVsXSMOIk4
#=========================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        p1,p2=l1,l2
        head=ListNode(0)
        temp=head
        while p1!=None or p2!=None:
            sm=0
            if p1!=None:
                sm+=p1.val
                p1=p1.next
            if p2!=None:
                sm+=p2.val
                p2=p2.next
            sm+=c
            temp.next=ListNode(sm%10)
            temp=temp.next
            c=sm//10
        if c!=0:
            temp.next=ListNode(c)
        return head.next

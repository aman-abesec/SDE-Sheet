#======================================================
#      160. Intersection of Two Linked Lists
#      https://leetcode.com/problems/intersection-of-two-linked-lists/
#      https://youtu.be/u4FWXfgS8jw
#=========================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1,t2=headA,headB
        while t1!=None or t2!=None:
            if t1==None:
                t1=headB
            if t2==None:
                t2=headA
            if t1==t2:
                return t1
            t1=t1.next
            t2=t2.next
        return 

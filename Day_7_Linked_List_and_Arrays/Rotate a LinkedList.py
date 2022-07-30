#======================================================
#      61. Rotate List
#      https://leetcode.com/problems/rotate-list/description/
#      https://youtu.be/ysytSSXpAI0
#=========================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        l=0
        temp=head
        prev=head
        while temp:
            prev=temp
            temp=temp.next
            l+=1
        prev.next=head
        k=k%l
        curr=head
        for i in range(l-k-1):
            curr=curr.next
        head=curr.next
        curr.next=None
        return head

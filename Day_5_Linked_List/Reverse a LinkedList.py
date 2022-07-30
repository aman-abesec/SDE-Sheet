#======================================================
#      206. Reverse Linked List
#      https://leetcode.com/problems/reverse-linked-list/
#      https://youtu.be/iRtLEoL-r-g
#=========================================================
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        prev=None
        curr=head
        while curr:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        return prev

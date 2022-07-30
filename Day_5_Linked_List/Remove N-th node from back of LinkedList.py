#======================================================
#      19. Remove Nth Node From End of List
#      https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#      https://youtu.be/jyjfroqmWvQ
#=========================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None: return None
        s,f=head,head
        c=0
        while f:
            if n<c:
                s=s.next
            f=f.next
            c+=1
        if n==c:
            return head.next
        else:
            s.next=s.next.next
        return head

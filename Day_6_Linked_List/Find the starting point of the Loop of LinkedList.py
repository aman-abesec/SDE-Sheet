#======================================================
#      142. Linked List Cycle II
#      https://leetcode.com/problems/linked-list-cycle-ii/
#      https://youtu.be/QfbOhn0WZ88
#=========================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:return None
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                temp=head
                while slow!=temp:
                    slow=slow.next
                    temp=temp.next
                return temp

        return None

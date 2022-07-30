#======================================================
#      876. Middle of the Linked List
#      https://leetcode.com/problems/middle-of-the-linked-list/
#      https://youtu.be/sGdwSH8RK-o
#=========================================================
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and slow!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

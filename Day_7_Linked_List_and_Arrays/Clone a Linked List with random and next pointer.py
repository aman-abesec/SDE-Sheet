#======================================================
#      138. Copy List with Random Pointer
#      https://leetcode.com/problems/copy-list-with-random-pointer/
#      https://youtu.be/4apaOcK586U
#=========================================================
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return head
        #Creating new Node between each node
        curr=head
        while curr:
            temp=curr.next
            curr.next=Node(curr.val)
            curr.next.next=temp
            curr=temp
        curr=head
        while curr!=None:
            if curr.next:
                if curr.random!=None:
                    curr.next.random=curr.random.next
                else:
                    curr.next.random=None
            curr=curr.next.next
        ohead=head
        chead=head.next
        curr=chead
        while ohead:
            ohead.next=ohead.next.next
            if ohead.next==None:
                chead.next=None
                break
            chead.next=chead.next.next
            ohead=ohead.next
            chead=chead.next
        return curr

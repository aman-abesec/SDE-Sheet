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


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Insert copied nodes after original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            copied_node = curr.next

            if curr.random:
                copied_node.random = curr.random.next

            curr = copied_node.next

        # Step 3: Separate original and copied list
        curr = head
        copied_head = head.next

        while curr:
            copied_node = curr.next
            curr.next = copied_node.next

            if copied_node.next:
                copied_node.next = copied_node.next.next

            curr = curr.next

        return copied_head
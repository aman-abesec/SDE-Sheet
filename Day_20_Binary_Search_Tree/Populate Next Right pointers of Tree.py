#===========================================================
#116. Populating Next Right Pointers in Each Node
#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#https://youtu.be/3MRPQFUpoA0
#==============================================================

#using extra space
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def solve(root):
            if root==None:return root
            q=deque()
            q.append(root)
            while q:
                l=len(q)
                u=None
                for i in range(l):
                    if u!=None:
                        v=q.popleft()
                        u.next=v
                        u=v
                    else:
                        u=q.popleft()
                    if u.left!=None:q.append(u.left)
                    if u.right!=None:q.append(u.right)
                u.next=None
            return root
        return solve(root)

#Without using extra space
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        temp_node=root
        while temp_node!=None and temp_node.left!=None:
            node=temp_node
            while True:
                node.left.next=node.right
                if node.next==None:break
                node.right.next=node.next.left
                node=node.next
            temp_node=temp_node.left
        return root

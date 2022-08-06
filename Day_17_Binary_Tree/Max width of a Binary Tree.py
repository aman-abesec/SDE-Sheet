#=============================================
#   662. Maximum Width of Binary Tree
#https://leetcode.com/problems/maximum-width-of-binary-tree/
#https://youtu.be/ZbybYvcVLks
#============================================

from collections import deque
class Solution:
    def solve(self,head):
        if head==None:return 1
        q=deque()
        mx=-1
        q.append([head,1])
        while q:
            l=len(q)
            mn=q[0][1]
            fi,li=0,0
            for i in range(l):
                cid=q[0][1]-mn
                node,index=q.popleft()
                if i==0:
                    fi=cid
                if i==l-1:
                    li=cid
                if node.left!=None:q.append([node.left,2*cid+1])
                if node.right!=None:q.append([node.right,2*cid+2])
            mx=max(mx,(li-fi+1))
        return mx

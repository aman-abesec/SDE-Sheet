#=============================================
#   Bottom View of Binary Tree
#https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
#https://youtu.be/0FtVY6I4pB8
#============================================

#T-O(n)
#S-O(n)
from collections import deque
class Solution:
    def bottomView(self, root):
        ans=[]
        if root==None:return ans
        hash_map={}
        q=deque()
        hash_map[0]=root
        q.append([root,0])
        while q:
            l=len(q)
            n,k=q.popleft()
            hash_map[k]=n
            if n.left!=None:q.append([n.left,k-1])
            if n.right!=None:q.append([n.right,k+1])
        # hash_map.sort()
        for v in sorted(hash_map):
            ans.append(hash_map[v].data)
        return ans

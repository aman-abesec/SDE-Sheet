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
        q = deque()
        hash_map = {}
        q.append([root,0])
        while q:
            node,index = q.popleft()
            hash_map[index]= node.data
            if node.left!=None:q.append([node.left,index-1])
            if node.right!=None:q.append([node.right,index+1])
        ans = []
        for v in sorted(hash_map):
            ans.append(hash_map[v])
        return ans

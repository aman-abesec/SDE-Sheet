#=============================================
#   236. Lowest Common Ancestor of a Binary Tree
#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#============================================

#T-O(n)
#S-O(height)
class Solution:
    def solve(self,root,p,q):
        if root==None:return None
        if root==p or root==q:return root
        l=self.solve(root.left,p,q)
        r=self.solve(root.right,p,q)
        if l==None and r==None:return None
        if l==None:return r
        if r==None:return l
        if l!=None and r!=None:return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)
    
    
#Gfg Soluation
class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        def solve(root,n1,n2):
            if root==None or root.data==n1 or root.data==n2:
                return root
            l=solve(root.left,n1,n2)
            r=solve(root.right,n1,n2)
            if l!=None and r!=None:return root
            if l==None:return r
            if r==None:return l
        return solve(root,n1,n2)

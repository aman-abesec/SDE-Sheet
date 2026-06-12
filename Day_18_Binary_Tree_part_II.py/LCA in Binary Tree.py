#=============================================
#   236. Lowest Common Ancestor of a Binary Tree
#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#.  https://www.youtube.com/watch?v=cOjLyASDJcc&t=451s
#============================================

#T-O(n)
#S-O(height)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root,p,q):
            if root == None: return None
            if(root==p or root==q):return root
            l=lca(root.left,p,q)
            r=lca(root.right,p,q)
            if l==None:return r
            if r==None:return l
            return root
        return lca(root,p,q)
    
    
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

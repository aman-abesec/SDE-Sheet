#=============================================
#   Boundary Traversal of binary tree
#  https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
#============================================
class Solution:
    def printBoundaryView(self, root):
        def isleaf(root):
            if root==None or root==None:return False
            if root.left==None and root.right==None:return True
            return False
        def addleft(root,ans):
            root=root.left
            while root:
                if isleaf(root)==False:ans.append(root.data)
                if root.left:root=root.left
                else:root=root.right
        def addleaf(root,ans):
            if root==None:return
            if isleaf(root):
                ans.append(root.data)
            addleaf(root.left,ans)
            addleaf(root.right,ans)
        def addright(root,ans):
            temp=[]
            root=root.right
            while root:
                if isleaf(root)==False:temp.append(root.data)
                if root.right:root=root.right
                else:root=root.left
            while temp:
                ans.append(temp.pop())
        ans=[]
        if root==None:return ans
        if isleaf(root)==False:ans.append(root.data)
        addleft(root,ans)
        addleaf(root,ans)
        addright(root,ans)
        return ans

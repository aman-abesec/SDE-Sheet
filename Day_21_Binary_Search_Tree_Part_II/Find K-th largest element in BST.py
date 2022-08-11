#=====================================================
#Kth largest element in BST
#https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1
#======================================================

class Solution:
    def kthLargest(self,root, k):
        def height(root):
            if root==None:return 0
            return 1+height(root.left)+height(root.right)
        def solve(root,k,ans):
            if root==None:return
            solve(root.left,k,ans)
            ans[0]+=1
            if ans[0]==k:
                ans[1]=root
                return
            solve(root.right,k,ans)
        ans=[0,None]
        solve(root,height(root)-k+1,ans)
        return ans[1].data

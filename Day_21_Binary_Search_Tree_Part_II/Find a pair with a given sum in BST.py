#=====================================================
#653. Two Sum IV - Input is a BST
#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
#======================================================

#Method-1
#T-O(n)
#S-O(n)
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def solve(root,stack):
            if root==None:return
            solve(root.left,stack)
            stack.append(root.val)
            solve(root.right,stack)
        stack=[]
        solve(root,stack)
        s,e=0,len(stack)-1
        while e>s:
            if stack[e]+stack[s]>k:
                e-=1
            elif stack[e]+stack[s]<k:
                s+=1
            else:
                return True
        return False

#Method-2
#T-O(n)
#S-O(2*h)
class BSTIterr:
    def __init__(self,root,flag):
        self.stack=[]
        self.flag=flag
        #self.root=root
        self.push(root)
    def next(self):
        node=self.stack.pop()
        if self.flag==True:
            self.push(node.right)
        else:
            self.push(node.left)
        return node.val
    def push(self,node):
        while node!=None:
            self.stack.append(node)
            if self.flag==True:
                node=node.left
            elif self.flag==False:
                node=node.right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root==None:return False
        b1=BSTIterr(root,True)
        b2=BSTIterr(root,False)
        i=b1.next()
        j=b2.next()
        while i<j:
            if i+j==k:return True
            elif i+j>k:
                j=b2.next()
            else:
                i=b1.next()
        return False

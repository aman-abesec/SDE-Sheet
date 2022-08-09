#===========================================================
#Predecessor and Successor
#https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1
#==============================================================

def findPreSuc(root, pre, suc, key):
    def solve(r,key,suc,pre):
        s=None
        root=r
        while root!=None:
            if root.key<=key:
                root=root.right
            else:
                s=root
                root=root.left
        p=None
        r2=r
        while r2!=None:
            if r2.key<key:
                p=r2
                r2=r2.right
            else:
                r2=r2.left

        pre[0]=p
        suc[0]=s
    solve(root,key,suc,pre)

#=============================================
#   Children Sum Parent
#   https://practice.geeksforgeeks.org/problems/children-sum-parent/1
#============================================

def floorBst(root,tar):
    ans=-1
    while root:
        if root.data==tar:
            ans=root.data
            break
        if root.data<tar:
            root=root.right
        else:
            ans=root.data
            root=root.left
    return ans

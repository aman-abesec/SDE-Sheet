
def ceilBst(root,tar):
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

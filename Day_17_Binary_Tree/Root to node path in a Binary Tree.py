#=================================================
#Root to node path
#=================================================
def rootToNode(root,data,q):
    if root==None:return False
    q.append(root.val)
    if root.val==data:
        return True
    if rootToNode(root.left,data,q)==True or rootToNode(root.right,data,q)==True:
        return True
    q.pop()
    return False

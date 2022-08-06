#=============================================
#   Left View of Binary Tree
#https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
#============================================

#Method-1
#T-O(n)
#S-O(maxwidth of tree)
def LeftView(root):
    result=[]
    q=deque()
    if root==None:return result
    q.append(root)
    while q:
        l=len(q)
        for i in range(l):
            t=q.popleft()
            if i==0:
                result.append(t.data)
            if t.left!=None:q.append(t.left)
            if t.right!=None:q.append(t.right)
    return result

#Method-2
#T-O(n)
#S-O(height of tree)
def LeftView(root):
    ans=[]
    def solve(root,i):
        if root==None:
            return
        if len(ans)<i:
            ans.append(root.data)
        solve(root.left,i+1)
        solve(root.right,i+1)
    solve(root,1)
    return ans

#=============================================
#   Preorder Inorder Postorder Traversals in One Traversal
#https://youtu.be/ySp2epYvgTE
#============================================

#Method-1
#T-O(3*N)
#S-O(3*N)
def printInPrePost(root):
    stack=[[root,1]]
    In=[]
    Pre=[]
    post=[]
    while stack:
        node,val=stack[-1]
        if val==1:
            Pre.append(node.val)
            stack[-1][1]+=1
            if node.left!=None:
                stack.append([node.left,1])
        elif val==2:
            In.append(node.val)
            stack[-1][1]+=1
            if node.right!=None:
                stack.append([node.right,1])
        else:
            Post.append(node.val)
            stack.pop()
    print(In,Pre,Post)

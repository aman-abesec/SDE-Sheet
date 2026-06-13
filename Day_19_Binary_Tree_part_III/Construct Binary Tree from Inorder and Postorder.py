#=============================================
#   106. Construct Binary Tree from Inorder and Postorder Traversal
#  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#============================================

postIndex=0
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(In,Post,s,e):
            global postIndex
            if e<s:return None
            root=TreeNode(Post[postIndex])
            postIndex-=1
            index=0
            for i in range(s,e+1):
                if root.val==In[i]:
                    index=i
                    break
            root.right=solve(In,Post,index+1,e)
            root.left=solve(In,Post,s,index-1)
            return root
        global postIndex
        postIndex=len(postorder)-1
        return solve(inorder,postorder,0,postIndex)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self,inorder: List[int],postorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i, value in enumerate(inorder):
            index_map[value] = i
        postIndex = len(postorder) - 1

        def solve(start, end):
            nonlocal postIndex

            if start > end:return None

            root_val = postorder[postIndex]
            postIndex -= 1
            root = TreeNode(root_val)
            mid = index_map[root_val]
            root.right = solve(mid + 1, end)
            root.left = solve(start, mid - 1)

            return root

        return solve(0, len(inorder) - 1)


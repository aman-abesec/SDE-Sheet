#=============================================
#   105. Construct Binary Tree from Preorder and Inorder Traversal
#  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#============================================

#Note:>Time complexcitycan be reduce if we use hash_map
#T-O(n^2)
preIndex=0
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solve(Pre,In,s,e):
            if s>e:return None
            global preIndex
            root=TreeNode(Pre[preIndex])
            preIndex+=1
            new_start=0
            for i in range(s,e+1):
                if root.val==In[i]:
                    new_start=i
                    break
            root.left=solve(Pre,In,s,new_start-1)
            root.right=solve(Pre,In,new_start+1,e)
            return root
        global preIndex
        preIndex=0
        return solve(preorder,inorder,preIndex,len(preorder)-1)

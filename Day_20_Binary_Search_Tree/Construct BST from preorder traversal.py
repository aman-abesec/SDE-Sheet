#===========================================================
#1008. Construct Binary Search Tree from Preorder Traversal
#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
#https://youtu.be/UmJT3j26t1I
#==============================================================

#Note:>inorder of binary search tree is sorted
i=0
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def solve(nums,bound,length):
            global i
            if i==length or nums[i]>bound:return None
            node=TreeNode(nums[i])
            i+=1
            node.left=solve(nums,node.val,length)
            node.right=solve(nums,bound,length)
            return node
        bound=math.inf
        global i
        i=0
        return solve(preorder,bound,len(preorder))

#=============================================
#   102. Binary Tree Level Order Traversal
#https://leetcode.com/problems/binary-tree-level-order-traversal/
#============================================
#T-O(n)
#S-O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:return []
        result=[]
        q=deque()
        q.append(root)
        while q:
            l=len(q)
            temp=[]
            for i in range(l):
                node=q.popleft()
                temp.append(node.val)
                if node.left!=None:q.append(node.left)
                if node.right!=None:q.append(node.right)
            result.append(temp)
        return result

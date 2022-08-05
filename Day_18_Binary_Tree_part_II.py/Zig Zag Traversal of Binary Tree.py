#=============================================
#   103. Binary Tree Zigzag Level Order Traversal
#  https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#============================================

class Solution:
    def solve(self,root):
        if root==None:return []
        result=[]
        stack=[]
        q=deque()
        flag=False
        q.append(root)
        while q:
            temp=[]
            l=len(q)
            for i in range(l):
                node=q.popleft()
                if flag:
                    stack.append(node.val)
                else:
                    temp.append(node.val)
                if node.left!=None:q.append(node.left)
                if node.right!=None:q.append(node.right)
            if flag:
                while stack:
                    temp.append(stack.pop())
            result.append(temp)
            flag=~flag
        return result


    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.solve(root)

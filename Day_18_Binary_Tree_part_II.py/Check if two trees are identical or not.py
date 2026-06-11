#=============================================
#   100. Same Tree
#   https://leetcode.com/problems/same-tree/
#============================================

#T-O(n)
#S-O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if node1 is None and node2 is None:return True
            if node1 is None or node2 is None or node1.val != node2.val:return False
            return (
                isSame(node1.left, node2.left)
                and isSame(node1.right, node2.right)
            )

        return isSame(p, q)

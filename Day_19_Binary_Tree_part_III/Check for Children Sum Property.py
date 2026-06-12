#=============================================
#   Children Sum Parent
#   https://practice.geeksforgeeks.org/problems/children-sum-parent/1
#============================================

class Solution:
    def isSumProperty(self, root):
        if root is None:return True
        if root.left is None and root.right is None:return True

        left_value = root.left.data if root.left else 0
        right_value = root.right.data if root.right else 0

        return (
            root.data == left_value + right_value
            and self.isSumProperty(root.left)
            and self.isSumProperty(root.right)
        )

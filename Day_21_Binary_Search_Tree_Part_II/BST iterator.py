#=====================================================
#173. Binary Search Tree Iterator
#https://leetcode.com/problems/binary-search-tree-iterator/
#======================================================

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.addVal(root)
    def next(self) -> int:
        if self.stack==[]:return False
        temp=self.stack.pop()
        self.addVal(temp.right)
        return temp.val

    def addVal(self,root):
        if root==None:return
        self.stack.append(root)
        self.addVal(root.left)

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False

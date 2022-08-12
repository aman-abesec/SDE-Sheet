#=====================================================
#297. Serialize and Deserialize Binary Tree
#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#================================================================
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans=[]
        def solve(root):
            if root==None:
                ans.append(str('N'))
                return
            ans.append(str(root.val))
            solve(root.left)
            solve(root.right)
        solve(root)
        return  ",".join(ans)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def solve(num,ind):
            if ind[0]==len(num):return None
            val=num[ind[0]]
            ind[0]+=1
            if val=='N':return None
            root=TreeNode(int(val))
            root.left=solve(num,ind)
            root.right=solve(num,ind)
            return root
        num=data.split(',')
        ind=[0]
        return solve(num,ind)

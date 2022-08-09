#===========================================================
#108. Convert Sorted Array to Binary Search Tree
#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#==============================================================

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(nums,s,e):
            if s>e:return None
            mid=(s+e)//2
            node=TreeNode(nums[mid])
            node.left=solve(nums,s,mid-1)
            node.right=solve(nums,mid+1,e)
            return node
        return solve(nums,0,len(nums)-1)

#======================================================
#      46. Permutations
#      https://leetcode.com/problems/permutations/
#      https://youtu.be/f2ic2Rsc9pU
#=========================================================
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def allpermute(num,ind=0):
            if ind==len(num)-1:
                n=[m for m in num]
                result.append(n)
                return
            else:
                for i in range(ind,len(num)):
                    num[ind],num[i]=num[i],num[ind]
                    allpermute(num,ind+1)
                    num[ind],num[i]=num[i],num[ind]
        allpermute(nums)
        return result

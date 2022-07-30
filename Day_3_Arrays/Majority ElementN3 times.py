#======================================================
#      229. Majority Element II
#   https://leetcode.com/problems/majority-element-ii/
#   https://youtu.be/AoX3BPWNnoE
#=========================================================
#T-O(n)
#S-O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        hash_map=dict()
        l=len(nums)
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        for key,val in hash_map.items():
            if val>l//3:
                result.append(key)
        return result

#T-O(n)+O(n)
#S-O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1=-1
        n3=-1
        c1=0
        c2=0
        for i in nums:
            if i==n1:
                c1+=1
            elif i==n3:
                c2+=1
            elif c1==0:
                n1=i
                c1=1
            elif c2==0:
                n3=i
                c2=1
            else:
                c1-=1
                c2-=1
        c1,c2=0,0
        for i in nums:
            if i==n1:
                c1+=1
            elif i==n3:
                c2+=1
        result=[]
        if c1>len(nums)//3:
            result.append(n1)
        if c2>len(nums)//3:
            result.append(n3)
        return result

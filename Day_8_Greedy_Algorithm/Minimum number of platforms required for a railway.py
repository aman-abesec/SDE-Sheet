#======================================================
#      Minimum Platforms
#      https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
#      https://youtu.be/dxVcMDI7vyI
#=========================================================
class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i,j=1,0
        mx=1
        plt=1
        while i<n and j<n:
            if arr[i]<=dep[j]:
                i+=1
                plt+=1
            elif arr[i]>dep[j]:
                j+=1
                plt-=1
            if plt>mx:
                mx=plt
            # mx=max(mx,plt)
        return mx

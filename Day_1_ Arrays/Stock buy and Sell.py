#======================================================
#           121. Best Time to Buy and Sell Stock
#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  https://youtu.be/eMSfBgbiEjk
#=========================================================
#s=O(1)
# T=O(n^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                mx=max(mx,prices[j]-prices[i])
        return mx

#S=O(1)
#T-O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        mn=prices[0]
        for i in range(len(prices)):
            mn=min(mn,prices[i])
            mx=max(mx,prices[i]-mn)
        return mx

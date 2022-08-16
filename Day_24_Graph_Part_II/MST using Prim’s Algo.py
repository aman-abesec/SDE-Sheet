#=====================================================
#Minimum Spanning Tree
#https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
#================================================================

import math
import heapq
class Solution:
    def spanningTree(self, V, adj):
        minheap=[]
        heapq.heappush(minheap,[0,0])
        result=0
        visit=set()
        # visit.add(0)
        while minheap:
            wt,u=heapq.heappop(minheap)
            if u not in visit:
                visit.add(u)
                result+=wt
                for v in adj[u]:
                    if  v[0] not in visit:
                        heapq.heappush(minheap,[v[1],v[0]])
        return result

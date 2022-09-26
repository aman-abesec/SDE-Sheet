#=====================================================
#Minimum Spanning Tree
#https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
#================================================================
class Solution:
    def spanningTree(self, V, adj):
        adjMat=[[0 for __ in range(V)] for _ in range(V)]
        for i in range(V):
            for v in adj[i]:
                adjMat[i][v[0]]=v[1]
        # print(adjMat)
        dis=[math.inf for _ in range(V)]
        dis[0]=0
        vis=[0 for _ in range(V)]
        result=0
        for i in range(V):
            u=-1
            for k in range(V):
                if vis[k]==0 and (u==-1 or dis[u]>dis[k]):
                    u=k
            vis[u]=1
            result+=dis[u]
            for v in range(V):
                if adjMat[u][v]!=0 and vis[v]==0:
                    dis[v]=min(dis[v],adjMat[u][v])

        return result
 #Method -2
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

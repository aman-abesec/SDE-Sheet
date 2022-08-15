#=====================================================
#Implementing Dijkstra Algorithm
#https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
#================================================================

import math
import heapq
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist=[math.inf for _ in range(V)]
        dist[S]=0
        minheap=[]
        heapq.heappush(minheap,[dist[S],S])
        while minheap:
            dis,node=heapq.heappop(minheap)
            for v in adj[node]:
                if dist[v[0]]>dis+v[1]:
                    dist[v[0]]=dis+v[1]
                    heapq.heappush(minheap,[dist[v[0]],v[0]])
        return dist

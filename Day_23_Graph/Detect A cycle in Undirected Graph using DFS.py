#=====================================================
#Detect cycle in an undirected graph
#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
#================================================================

from collections import deque

class Solution:
	def isCycle(self, V, adj):
		def cycle(s,visited,adj,prev):
            visited[s]=True
            for v in adj[s]:
                if visited[v]==False:
                    if cycle(v,visited,adj,s):return True
                elif visited[v]==True and v!=prev:return True
            return False
        def solve(v,adj):
            visited=[False for _ in range(v+1)]
            for i in range(0,v):
                if visited[i]==False:
                    if cycle(i,visited,adj,-1):
                        return True
            return False

        return solve(V,adj)

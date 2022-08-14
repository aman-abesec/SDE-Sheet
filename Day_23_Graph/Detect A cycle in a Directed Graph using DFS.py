#=====================================================
#Detect cycle in an undirected graph
#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
#================================================================

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        def dfs(s,adj,visited,dfsVisited,v):
            visited[s]=True
            dfsVisited[s]=True
            for v in adj[s]:
                if visited[v]==False:
                    if dfs(v,adj,visited,dfsVisited,v):return True
                if visited[v]==True and dfsVisited[v]==True:
                    return True
            dfsVisited[s]=False
            return False
        def solve(V,adj):
            visited=[False for _ in range(V+1)]
            dfsVisited=[False for _ in range(V+1)]
            for i in range(V):
                if visited[i]==False:
                    if dfs(i,adj,visited,dfsVisited,V):return True
            return False
        return solve(V,adj)

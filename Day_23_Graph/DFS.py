#=====================================================
#DFS of Graph
#https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
#================================================================

class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V,adj):
        def solve(s,V,adj,stack,visited):
            stack.append(s)
            visited[s]=True
            for v in adj[s]:
                if visited[v]==False:
                    solve(v,V,adj,stack,visited)
        stack=[]
        visited=[False for _ in range(V+1)]
        solve(0,V,adj,stack,visited)
        return stack

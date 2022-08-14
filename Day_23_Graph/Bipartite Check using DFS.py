#=====================================================
#785. Is Graph Bipartite?
#https://leetcode.com/problems/is-graph-bipartite/
#================================================================

from collections import deque
class Solution:
    def solve(self,u,color,adj):
        if u not in color:color[u]=0
        for v in adj[u]:
            if v in color and color[v]==color[u]:
                return False
            elif v not in color :
                color[v]=1-color[u]
                if self.solve(v,color,adj)==False:return False
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        for i in range(len(graph)):
            if i not in color:
                if self.solve(i,color,graph)==False:
                    return False
        return True

#=====================================================
#Strongly Connected Component(using KosaRaju’s algo)
#================================================================
def dfsPrint(u,adj,visited):
    visited[u]=True
    for v in adj[u]:
        if visited[v]==False:
            dfsPrint(v,adj,visited)
    print(u,end=" ")

def printGraph(adj,v):
    visited=[False for _ in range(v+1)]
    for u in range(v):
        if visited[u]==False:
            dfsPrint(u,adj,visited)
            print()

def reverseGraph(v,adj):
    new_Graph=[[] for _ in range(v)]
    for i in range(v):
        for j in adj[i]:
            new_Graph[j].append(i)
    return new_Graph

def dfs(u,adj,stack,visited):
    visited[u]=True
    for v in adj[u]:
        if visited[v]==False:
            dfs(v,adj,stack,visited)
    stack.append(u)

def kosaRaju(adj,v):
    visited=[False for _ in range(v+1)]
    stack=[]
    for u in range(v):
        if visited[u]==False:
            dfs(u,adj,stack,visited)
    new_Graph=reverseGraph(v,adj)
    printGraph(new_Graph,v)

adj=[[1],[2,3],[0],[4],[]]
vertex=5
kosaRaju(adj,vertex)

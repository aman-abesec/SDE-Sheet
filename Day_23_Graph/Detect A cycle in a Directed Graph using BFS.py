#=====================================================
#Detect cycle in an undirected graph
#https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
#================================================================

from collections import deque
class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        indegree=[0 for _ in range(V+1)]
        for i in range(V):
            for v in adj[i]:
                indegree[v]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        count=0
        while q:
            u=q.popleft()
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
            count+=1
        if count!=V:return True
        return False

    #=======================================================================
    #Course Schedule
    #https://leetcode.com/problems/course-schedule/submissions/
    #======================================================================
    class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList=[[] for _ in range(numCourses)]
        for k in prerequisites:
            adjList[k[0]].append(k[1])
        indegree=[0 for _ in range(numCourses)]
        for i in range(numCourses):
            for k in adjList[i]:
                indegree[k]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:q.append(i)
        count=0
        while q:
            u=q.popleft()
            for v in adjList[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
            count+=1
        return  numCourses==count
        

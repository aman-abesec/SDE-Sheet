#======================================================
#           56. Merge Intervals
#  https://leetcode.com/problems/merge-intervals/
#=========================================================
#sort the list first
# We have to handle mainly three cases
# case1: [1,3],[2,5]->[1,5]
# case1: [1,3],[5,6]->[1,3],[5,6]
# case1: [1,5],[2,3]->[1,5]
#T=O(nlog(n))+O(n)
#S=O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort()
        for i in range(len(intervals)):
            if result!=[] and result[-1][1]>=intervals[i][0] and result[-1][1]<=intervals[i][1]:
                t=result.pop()
                result.append([t[0],intervals[i][-1]])
            elif result!=[] and result[-1][1]>=intervals[i][0] and result[-1][1]>=intervals[i][1]:
                continue
            else:
                result.append(intervals[i])
        return result
# [[1,3],[2,6],[8,10],[15,18]]
# [[1,4],[4,5]]
# [[3,7],[5,8]]
# [[1,4],[0,4]]
# [[1,4],[2,3]]

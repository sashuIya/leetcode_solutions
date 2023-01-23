# Problem statement:
# https://leetcode.com/problems/course-schedule

# Solution illustration:
# https://github.com/sashuIya/leetcode_solutions/blob/master/images/207.course-schedule.png

def find_cycle(v, colors, edges):
    """ returns true if cycle is found """
    colors[v] = 1
    for u in edges[v]:
        if colors[u] == 1:
            return True
        if colors[u] == 0 and find_cycle(u, colors, edges):
            return True
    
    colors[v] = 2


class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for i in range(n)]
        for u, v in prerequisites:
            edges[u].append(v)
        
        # 0: not visited
        # 1: currently visiting
        # 2: visited
        colors = [0] * n
        for v in range(n):
            if colors[v] == 0:
                if find_cycle(v, colors, edges):
                    return False
        
        return True
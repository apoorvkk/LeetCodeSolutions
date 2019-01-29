from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        time_graph = defaultdict(dict)        
        for u, v, w in times:
            time_graph[u][v] = w
        
        
        pq = [(0, K)]
        max_total = 0
        visited = set()
        
        while pq:
            curr_dist, curr_node = heappop(pq)
            if curr_node in visited: continue
                
            visited.add(curr_node)
            
            
            max_total = max(max_total, curr_dist)
            
            for neighbour_node, neighbour_weight in time_graph[curr_node].items():
                if neighbour_node not in visited:
                    heappush(pq, (curr_dist + neighbour_weight, neighbour_node))
        
        if len(visited) != N:
            return -1
        return max_total
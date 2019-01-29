from heapq import heappush, heappop
from collections import defaultdict

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        flight_graph = defaultdict(dict)
        
        for a, b, weight in flights:
            flight_graph[a][b] = weight
            
        pq = []
        heappush(pq, (0, 0, src)) # (dist, num stops, city)
        visited = set()
        
        while pq:
            curr_dist, curr_stops, curr_city = heappop(pq)
                
            if curr_city == dst:
                return curr_dist    
            
            if curr_stops >= K+1: continue
        
            visited.add(curr_city)
            
            for neighbour_city, neighbour_weight in flight_graph[curr_city].items():
                if neighbour_city not in visited:
                    heappush(pq, (curr_dist+neighbour_weight, curr_stops+1, neighbour_city))
            
        return -1

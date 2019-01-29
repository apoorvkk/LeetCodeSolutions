from collections import defaultdict

class Solution:
    def _create_graph(self, flights):
        graph = defaultdict(set)
        
        for city, connecting_cities in enumerate(flights):
            for i, m in enumerate(connecting_cities):
                if m == 1:
                    graph[city].add(i)
            graph[city].add(city)

        return graph
    
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        N = len(flights)
        K = len(days[0])
        old_vac_days = [0 for i in range(N)]
        vac_days = [0 for i in range(N)]
        city_graph = self._create_graph(flights)
        
        for i in range(K-1, -1, -1):
            for j in range(N):
                for h, m in enumerate(city_graph[j]):
                    new_days = days[m][i]
                    if i < K-1:
                        new_days += old_vac_days[m]
                        
                    if h > 0:
                        vac_days[j] = max(vac_days[j], new_days)
                    else:
                        vac_days[j] = new_days
            old_vac_days = vac_days
            vac_days = [0 for i in range(N)]
        
        return old_vac_days[0]
        
        
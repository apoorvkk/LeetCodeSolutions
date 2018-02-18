'''
URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
Time complexity: O(v+e)
Space complexity: O(v)
'''

from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self, n):
        self.graph = [defaultdict(int) for i in range(n)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def __getitem__(self, index):
        return self.graph[index]

    def reset_node(self, index):
        self.graph[index] = defaultdict(int)

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        graph = Graph(n)
        for edge in flights:
            graph.add_edge(*edge)

        self.remove_flights_longer_than_k_steps(k, graph, src, n)


        distances = [float("inf") for i in range(n)]
        visited_nodes = [False for i in range(n)]
        distances[src] = 0

        pq = []
        heapq.heappush(pq, (distances[src], src))

        while pq:
            dist, curr_node = heapq.heappop(pq)

            if not visited_nodes[curr_node]:
                visited_nodes[curr_node] = True

                for neighbour_node in graph[curr_node]:
                    if dist + graph[curr_node][neighbour_node] < distances[neighbour_node]:
                        distances[neighbour_node] = dist + graph[curr_node][neighbour_node]
                        heapq.heappush(pq, (distances[neighbour_node], neighbour_node))

        if distances[dst] == float("inf"):
            return -1
        return distances[dst]


    def remove_flights_longer_than_k_steps(self, k, graph, src, n): # K + 1
        queue = deque()
        not_visited_nodes = {i for i in range(n)}
        queue.append((src, 0))
        not_visited_nodes.remove(src)

        while len(queue) > 0:
            curr_node, dist = queue.popleft()

            if dist >= k+1: # Delete all neighbour node edges
                graph.reset_node(curr_node)
            else:
                for neighbour_node in graph[curr_node]:
                    if neighbour_node in not_visited_nodes:
                        not_visited_nodes.remove(neighbour_node)
                        queue.append((neighbour_node, dist+1))

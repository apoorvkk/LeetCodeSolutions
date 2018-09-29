'''
URL: https://leetcode.com/problems/possible-bipartition
Time complexity: O(V+E)
Space complexity: O(V+E)
'''

from collections import defaultdict

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(set)

        for edge in dislikes:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited = {}

        for node in range(1, N+1):
            if node not in visited and not self.dfs(node, visited, graph, 0, None):
                return False
        return True

    def dfs(self, curr_node, visited, graph, distance, prev_node):
        distance += 1
        visited[curr_node] = distance

        for child_node in graph[curr_node]:
            if child_node == prev_node:
                continue
            if child_node in visited: # cyclic
                if (distance - visited[child_node] + 1) % 2 == 1: # odd length
                    return False
            elif not self.dfs(child_node, visited, graph, distance, curr_node):
                return False

        return True

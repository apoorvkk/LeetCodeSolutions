'''
URL: https://leetcode.com/problems/evaluate-division/
Time complexity: O(m * (V+E)) m = number of queries, V = number of unique variables, E = number of equations
Space complexity: O(V+E) same variables as above
'''

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = self._construct_graph(equations, values)

        answers = []
        for i in range(len(queries)):
            answers.append(self._dfs(queries[i][0], queries[i][1], set(), graph, 1.0))

        return answers

    def _dfs(self, curr_node, end_node, visited, graph, curr_coefficient):
        if curr_node == end_node and curr_node in graph:
            return curr_coefficient

        visited.add(curr_node)
        for neighbour_node, edge_val in graph[curr_node].iteritems():
            if neighbour_node in visited:
                continue

            neighbour_coefficient = edge_val * curr_coefficient
            val = self._dfs(neighbour_node, end_node, visited, graph, neighbour_coefficient)
            if val != -1.0:
                return val

        return -1.0

    def _construct_graph(self, equations, values):
        graph = defaultdict(dict)

        for i in range(len(equations)):
            var_one, var_two = equations[i]
            curr_val = values[i]

            graph[var_one][var_two] = float(curr_val)
            graph[var_two][var_one] = 1.0 / curr_val

        return graph



'''
BFS VERSION

from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = self._construct_graph(equations, values)

        answers = []
        for i in range(len(queries)):
            start_var = queries[i][0]
            end_var = queries[i][1]
            visited = set()
            answer = self.find_answer(start_var, end_var, visited, graph)
            answers.append(answer)

        return answers

    def find_answer(self, start_node, end_node, visited, graph):
        queue = deque()
        queue.append((start_node, 1.0))
        visited.add(start_node)

        while len(queue) > 0:
            curr_node, curr_coefficient = queue.popleft()

            if curr_node == end_node and curr_node in graph:
                return curr_coefficient

            for neighbour_node, edge_coeff in graph[curr_node].iteritems():
                new_coeff = curr_coefficient * edge_coeff

                if neighbour_node not in visited:
                    visited.add(neighbour_node)
                    queue.append((neighbour_node, new_coeff))
        return -1

    def _construct_graph(self, equations, values):
        graph = defaultdict(dict)

        for i in range(len(equations)):
            var_one, var_two = equations[i]
            curr_val = values[i]

            graph[var_one][var_two] = float(curr_val)
            graph[var_two][var_one] = 1.0 / curr_val

        return graph
'''

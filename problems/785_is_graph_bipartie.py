'''
URL: https://leetcode.com/problems/is-graph-bipartite/description/
Time complexity: O(v+e)
Space complexity: O(v)
'''

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        set_a = set()
        set_b = set()
        not_visited_nodes = set([i for i in range(len(graph))])

        next_nodes = []
        while len(not_visited_nodes) > 0 or len(next_nodes) > 0:
            if len(next_nodes) == 0:
                set_a, set_b = set(), set()
                curr_node = not_visited_nodes.pop()
                if len(graph[curr_node]) > 0:
                    set_a.add(curr_node)
                    for neighbour in graph[curr_node]:
                        set_b.add(neighbour)
                        next_nodes.append(neighbour)
                        not_visited_nodes.remove(neighbour)
            else:
                curr_node = next_nodes.pop()
                expected_set = set_a
                not_expected_set = set_b
                if curr_node in set_a:
                    expected_set, not_expected_set = not_expected_set, expected_set

                for neighbour in graph[curr_node]:
                    if neighbour in not_expected_set:
                        return False
                    else:
                        if neighbour in not_visited_nodes:
                            expected_set.add(neighbour)
                            next_nodes.append(neighbour)
                            not_visited_nodes.remove(neighbour)
        return True

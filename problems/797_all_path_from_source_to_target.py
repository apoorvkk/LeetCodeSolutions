'''
URL: https://leetcode.com/problems/all-paths-from-source-to-target/
Time complexity: O(E)
Space complexity: O(V)
'''

class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        paths = []
        self.find_paths(graph, paths, [0])

        return paths

    def find_paths(self, graph, paths, curr_path):
        curr_node = curr_path[-1]
        if curr_node == len(graph)-1:
            paths.append(curr_path)
        else:
            for child_node in graph[curr_node]:
                self.find_paths(graph, paths, curr_path + [child_node])

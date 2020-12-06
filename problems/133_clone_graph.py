'''
URL: https://leetcode.com/problems/clone-graph
Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return node

        queue = deque()
        seen_nodes = {}

        root_node = UndirectedGraphNode(node.label)
        queue.append((root_node, node))
        seen_nodes[root_node.label] = root_node

        while len(queue) > 0:
            curr_node, orig_node = queue.popleft()

            for orig_child_node in orig_node.neighbors:
                if orig_child_node.label not in seen_nodes:
                    new_child_node = UndirectedGraphNode(orig_child_node.label)
                    seen_nodes[new_child_node.label] = new_child_node
                    queue.append((new_child_node, orig_child_node))

                curr_node.neighbors.append(seen_nodes[orig_child_node.label])

        return root_node


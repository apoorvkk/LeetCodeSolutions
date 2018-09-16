'''
URL: https://leetcode.com/problems/short-encoding-of-words/description/
Time complexity: O(n*m)
Space complexity: O(n*m)
'''

class Node:
    def __init__(self, val, height):
        self.val = val
        self.height = height
        self.children = {}

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int

        ["time", "im", "bell"]

        S = "time#bell#"

        ["time", "ime", "med", "bell"]

        time#med#bell

        ["time", "imed", "bell"]
        "time#imed#"


        ["me", "time", "bell"]
        "time#bell#"
        0, 2, 5

        emi

                          .
                       e!   l
                    /        \
                  m!           l
                 /              \
                i                 e
               /                   \
               t                    b

        2. For each string, put into tree (in reverse order)
        3. Everytime you make a new path, add length of that path to a counter
        4. Return counter

        O(n * m)
        """
        # Create graph
        head = Node('', 0)
        for word in words:
            curr_node = head
            curr_height = 0
            for i in range(len(word)-1, -1, -1):
                curr_letter = word[i]
                curr_height += 1

                if curr_letter not in curr_node.children:
                    curr_node.children[curr_letter] = Node(curr_letter, curr_height)
                curr_node = curr_node.children[curr_letter]

        # Traverse graph
        compressed_string = 0
        stack = [head]
        while len(stack) > 0:
            curr_node = stack.pop()

            for child_letter, child_node in curr_node.children.iteritems():
                if len(child_node.children) == 0:
                    compressed_string += 1 + child_node.height
                else:
                    stack.append(child_node)

        return compressed_string


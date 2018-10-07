'''
URL: https://leetcode.com/problems/map-sum-pairs/
'''

class Node:
    def __init__(self, count=0):
        self.count = count
        self.childnodes = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.words = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.words:
            val = val - self.words[key]

        self.words[key] = val

        curr_node = self.head
        for char in key:
            if char in curr_node.childnodes:
                curr_node.childnodes[char].count += val
            else:
                curr_node.childnodes[char] = Node(val)

            curr_node = curr_node.childnodes[char]

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr_node = self.head

        for char in prefix:
            if char in curr_node.childnodes:
                curr_node = curr_node.childnodes[char]
            else:
                return 0
        return curr_node.count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

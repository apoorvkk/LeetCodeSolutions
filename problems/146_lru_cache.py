'''
URL: https://leetcode.com/problems/lru-cache
Time complexity: O(1)
Space complexity: O(n)
'''

class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0, 0)
        self.end = Node(0, 0)
        self.head.next = self.end
        self.end.prev = self.head
        self.lookup_table = {}

    def _add(self, node):
        end = self.end

        last_node = self.end.prev
        last_node.next = node
        node.prev = last_node

        node.next = end
        end.prev = node

    def _remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lookup_table:
            curr_node = self.lookup_table[key]

            self._remove(curr_node)
            self._add(curr_node)

            return curr_node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lookup_table: # set
            self._remove(self.lookup_table[key])
        else: # insertion
            if len(self.lookup_table) == self.capacity:
                n = self.head.next
                self._remove(n)

                del self.lookup_table[n.key]

        new_node = Node(key, value)
        self._add(new_node)
        self.lookup_table[key] = new_node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

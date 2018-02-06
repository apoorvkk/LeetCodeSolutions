'''
URL: https://leetcode.com/problems/nested-list-weight-sum/description/
Time complexity: O(n + mx) where n is number of int elements, m is max depth and x is number of general elements.
Space complexity: O(m) where m is max depth
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):

    def find_total(self, depth, nestedList):
        curr_sum = 0
        for elem in nestedList:
            if elem.isInteger():
                curr_sum += depth * elem.getInteger()
            else:
                curr_sum += self.find_total(depth+1, elem.getList())
        return curr_sum


    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None:
            return 0

        return self.find_total(1, nestedList)


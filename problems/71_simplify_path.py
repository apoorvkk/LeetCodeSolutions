'''
URL: https://leetcode.com/problems/simplify-path
Time complexity: O(n)
Space complexity: O(n)
'''


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        items = [p for p in path.split('/') if p != "." and p != ""]
        stack = []
        for item in items:
            if item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        return "/" + "/".join(stack)

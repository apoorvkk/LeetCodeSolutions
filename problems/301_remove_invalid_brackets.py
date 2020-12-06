'''
URL: https://leetcode.com/problems/remove-invalid-parentheses
Time complexity: O(2^n)
Space complexity: O(n!)
'''

from collections import deque

class Solution(object):
    def is_valid(self, s):
        open = 0
        for char in s:
            if char == "(":
                open += 1
            elif char == ")":
                if open == 0:
                    return False
                open -= 1
        return open == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue = deque()
        visited = set()

        queue.append(s)
        visited.add(s)

        valid_brackets = []
        found = False
        while len(queue) > 0:
            new_text = queue.popleft()

            if self.is_valid(new_text):
                valid_brackets.append(new_text)
                found = True

            if not found:
                for i in range(len(new_text)):
                    if new_text[i] not in ("(", ")"):
                        continue

                    removed_bracket_text = new_text[:i] + new_text[i+1:]
                    if removed_bracket_text not in visited:
                        visited.add(removed_bracket_text)
                        queue.append(removed_bracket_text)
        return valid_brackets

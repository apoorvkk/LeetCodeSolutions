'''
URL: https://leetcode.com/problems/basic-calculator/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def _get_next_num(self, i, s):
        curr_num = ""
        while i < len(s) and s[i].isdigit():
            curr_num += s[i]
            i += 1

        return i-1, int(curr_num)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [(0, 1)]
        prev_char = None
        i = 0
        while i < len(s):
            char = s[i]
            if char == ' ':
                i += 1
                continue

            if char.isdigit():
                i, num = self._get_next_num(i, s)

                if prev_char == '-':
                    stack[-1] = (stack[-1][0]-num, stack[-1][1])
                else:
                    stack[-1] = (stack[-1][0]+num, stack[-1][1])
            elif char == ')':
                val, sign = stack.pop()
                if len(stack) > 0:
                    stack[-1] = (stack[-1][0] + val * sign, stack[-1][1])
                else:
                    return val * sign
            elif char == '(':
                if prev_char == '-':
                    sign = -1
                else:
                    sign = 1
                stack.append((0, sign))

            prev_char = char
            i += 1

        if len(stack) > 0:
            return (stack[-1][0] * stack[-1][1])
        return -1

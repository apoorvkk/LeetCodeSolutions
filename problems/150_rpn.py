'''
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        answer = None
        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                val1 = int(stack.pop())
                val2 = int(stack.pop())

                if token == "+":
                    stack.append(val1 + val2)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "/":
                    val = abs(val2) // abs(val1)
                    if val1 < 0:
                        val *= -1
                    if val2 < 0:
                        val *= -1
                    stack.append(val)
            else:
                stack.append(token)

        return int(stack[0])

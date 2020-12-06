'''
URL: https://leetcode.com/problems/expression-add-operators
'''

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        expressions = []

        self.aux_add_operators(num, expressions, target, "", 0, 0, 0)
        return expressions

    def aux_add_operators(self, num, expressions, target, curr_expression, answer, start, prev_val):
        if start == len(num):
            if target == answer:
                expressions.append(curr_expression)
        else:
            for i in range(start, len(num)):
                if i > start and num[start] == '0':
                    break

                curr_number = int(num[start: i+1])
                if start == 0:
                    self.aux_add_operators(num, expressions, target, str(curr_number), curr_number, i+1, curr_number)
                else:
                    # add
                    new_expression = curr_expression + "+" + str(curr_number)
                    self.aux_add_operators(num, expressions, target, new_expression, answer+curr_number, i+1, curr_number)

                    # subtract
                    new_expression = curr_expression + "-" + str(curr_number)
                    self.aux_add_operators(num, expressions, target, new_expression, answer-int(curr_number), i+1, -curr_number)

                    # multiplication
                    new_expression = curr_expression + "*" + str(curr_number)
                    new_answer = answer - prev_val + prev_val * curr_number
                    new_prev_val = prev_val * curr_number
                    self.aux_add_operators(num, expressions, target, new_expression, new_answer, i+1, new_prev_val)

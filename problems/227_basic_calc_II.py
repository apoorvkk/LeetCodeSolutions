'''
URL: https://leetcode.com/problems/basic-calculator-ii/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def _get_next_num(self, s, i):
        number = 0
        while i < len(s) and s[i] in self.numbers:
            number = number * 10 + self.numbers[s[i]]
            i += 1
        return number, i

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_op = "+"
        i = 0
        self.numbers = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        self._get_next_num(s, 0)
        total = 0
        prev_num = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif s[i] in self.numbers:
                curr_num, next_index = self._get_next_num(s, i)
                i = next_index
                if prev_op == "+":
                    total += prev_num
                    prev_num = curr_num
                elif prev_op == "-":
                    total += prev_num
                    prev_num = -curr_num
                elif prev_op == "*":
                    prev_num = prev_num * curr_num
                else:
                    val = abs(prev_num) // curr_num
                    if prev_num < 0:
                        val *= -1
                    prev_num = val
            else:
                prev_op = s[i]
                i += 1

        total += prev_num
        return total

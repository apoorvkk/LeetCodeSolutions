'''
URL: https://leetcode.com/problems/multiply-strings/
Time complexity: O(m*n)
Space complexity: O(m+n)
'''

class Solution(object):
    def _multiply_by_one_digit(self, n, s):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        res = [0 for i in range(len(num1) + len(num2))]

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                multiplied_val = int(num1[i]) * int(num2[j])
                first_pos = i + j
                second_pos = i + j + 1

                total = multiplied_val + res[second_pos]

                res[second_pos] = total % 10
                res[first_pos] += total // 10

        res_str = "".join(map(lambda x: str(x), res))
        for i in range(len(res_str)):
            if res_str[i] != "0":
                return res_str[i:]
        return "0"

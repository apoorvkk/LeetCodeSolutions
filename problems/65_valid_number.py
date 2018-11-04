'''
URL: https://leetcode.com/problems/valid-number/
Time complexity: O(s) where s is length of string
Space complexity: O(n) where n is number of states
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
          {},
          {'blank': 1, 'sign': 2, 'digit':3, '.':4},
          {'digit':3, '.':4},
          {'digit':3, '.':5, 'e':6, 'blank':9},
          {'digit':5},
          {'digit':5, 'e':6, 'blank':9},
          {'sign':7, 'digit':8},
          {'digit':8},
          {'digit':8, 'blank':9},
          {'blank':9}
        ]
        curr_state = 1

        for c in s:
            if c == " ":
                c = 'blank'
            if c.isdigit():
                c = 'digit'
            if c in ['+', '-']:
                c = 'sign'

            if c not in state[curr_state]:
                return False
            curr_state = state[curr_state][c]

        if curr_state not in [3, 5, 8, 9]:
            return False
        return True

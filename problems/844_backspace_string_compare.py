'''
URL: https://leetcode.com/problems/backspace-string-compare
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):

    def next_char(self, curr_pos, s):
        num_backs = 0
        i = curr_pos - 1
        while i >= 0:
            if s[i] == '#':
                num_backs += 1
            elif num_backs == 0:
                return i
            elif num_backs > 0:
                num_backs -= 1

            i -= 1
        return -1

    def backspaceCompare(self, S, T):
        s_pos = self.next_char(len(S), S)
        t_pos = self.next_char(len(T), T)

        while s_pos >= 0 or t_pos >= 0:
            if s_pos == -1 or t_pos == -1:
                return False

            if S[s_pos] != T[t_pos]:
                return False

            s_pos = self.next_char(s_pos, S)
            t_pos = self.next_char(t_pos, T)

        return True

'''
URL: https://leetcode.com/problems/reverse-words-in-a-string
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        end = -1
        start = -1
        reversed_text = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                if end == -1:
                    start = i
                    end = i
                else:
                    start -= 1
            else:
                if end != -1:
                    word = s[start: end+1]
                    reversed_text += word
                    reversed_text += " "
                    start = -1
                    end = -1

        if end != -1:
            word = s[start: end+1]
            reversed_text += word

        return reversed_text.strip()


'''
URL: https://leetcode.com/problems/decode-string/description/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str


        3[abc]ef
         .
        repeats = 3
        """
        i, decoded = self._decode(s, 0, 1)
        return decoded

    def _decode(self, s, s_index, n_repeats):
        if s_index >= len(s):
            return s_index, ""

        text = ""
        i = s_index
        curr_repeats = ""
        while i < len(s):
            curr_char = s[i]

            if curr_char.isdigit():
                curr_repeats += curr_char
                i += 1
                continue
            elif curr_char == "[":
                i, decoded_substr = self._decode(s, i+1, int(curr_repeats))
                curr_repeats = ""
            elif curr_char == "]":
                i += 1
                break
            else:
                decoded_substr = curr_char
                i += 1

            text += decoded_substr

        return i, text * n_repeats


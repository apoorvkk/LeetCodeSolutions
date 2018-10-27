'''
URL: https://leetcode.com/problems/string-compression
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return 0

        curr_char = chars[0]
        count = 1
        new_string_pointer = 0

        j = 1
        while j <= len(chars):
            if j == len(chars) or curr_char != chars[j]:
                chars[new_string_pointer] = curr_char
                new_string_pointer += 1
                if count > 1:
                    for i, digit in enumerate(str(count)):
                        chars[new_string_pointer + i] = digit
                    new_string_pointer += len(str(count))
                count = 1
                if j < len(chars):
                    curr_char = chars[j]
            else:
                count += 1
            j += 1

        for i in range(len(chars) - new_string_pointer):
            chars.pop()

        return len(chars)

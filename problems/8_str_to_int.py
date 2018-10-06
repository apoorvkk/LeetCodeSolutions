'''
URL: https://leetcode.com/problems/string-to-integer-atoi/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def myAtoi(self, text):
        """
        :type str: str
        :rtype: int
        """
        if len(text) == 0:
            return 0
        numbers = {
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
        MAX_POS_NUM = 2**31 - 1
        MAX_NEG_NUM = 2**31
        is_negative = False
        starting_index = self.get_starting_num_index(text, numbers)

        if starting_index == -1:
            return 0

        if text[starting_index] in ("-", "+"):
            if starting_index + 1 >= len(text) or text[starting_index+1] not in numbers:
                return 0

            is_negative = True if text[starting_index] == "-" else False
            starting_index += 1

        final_num = 0
        curr_index = starting_index
        if is_negative:
            MAX_NUM = MAX_NEG_NUM
        else:
            MAX_NUM = MAX_POS_NUM
        while curr_index < len(text) and text[curr_index] in numbers:
            new_num = (final_num * 10) + numbers[text[curr_index]]
            if new_num > MAX_NUM:
                final_num = MAX_NUM
                break
            else:
                final_num = new_num

            curr_index += 1

        if is_negative:
            final_num *= -1
        return final_num

    def get_starting_num_index(self, text, numbers):
        i = 0
        while i < len(text):
            if text[i] == " ":
                i += 1
            else:
                if text[i] not in numbers and text[i] not in ("-", "+"):
                    return -1
                else:
                    return i
        return -1

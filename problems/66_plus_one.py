'''
URL: https://leetcode.com/problems/plus-one/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        [0, 0, 0]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)

        return digits

'''
URL: https://leetcode.com/problems/sum-of-subarray-minimums
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = [0 for i in range(len(A))]
        right = [0 for i in range(len(A))]
        stack_left = []
        stack_right = []

        # Compute left lengths
        # left[i] should hold the number of elements greater or equal to A[i] on its left hand side.
        for i in range(len(A)):
            curr_num = A[i]
            curr_length = 0
            while stack_left and stack_left[-1][0] >= curr_num:
                curr_length += stack_left.pop()[1] + 1

            left[i] = curr_length
            stack_left.append((curr_num, curr_length))

        # Compute right lengths
        # right[i] should hold the number of elements greater than A[i] on its right hand side.
        for i in range(len(A)-1, -1, -1):
            curr_num = A[i]
            curr_length = 0

            while stack_right and stack_right[-1][0] > curr_num:
                curr_length += stack_right.pop()[1] + 1

            right[i] = curr_length
            stack_right.append((curr_num, curr_length))

        total_sum = 0
        for i in range(len(A)):
            total_sum += A[i] * (left[i]+1) * (right[i]+1)

        return total_sum % (10**9 + 7)




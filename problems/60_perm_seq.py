'''
URL: https://leetcode.com/problems/permutation-sequence
Time complexity: O(n^2)
Space complexity: O(n)
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n+1)]
        facs = self.generate_factorials(n)

        result = ""
        size_of_perm = n
        while len(result) < size_of_perm:
            i = k / float(facs[n-1])

            if int(i) == i:
                i -= 1
            i = int(i)

            result += str(nums[i])
            del nums[i]

            k -= facs[n-1] * i
            n -= 1
        return result

    def generate_factorials(self, n):
        factorials = [1, 1]

        for i in range(2, n):
            factorials.append(factorials[-1] * i)
        return factorials

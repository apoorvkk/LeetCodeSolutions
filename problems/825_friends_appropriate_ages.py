'''
URL: https://leetcode.com/problems/friends-of-appropriate-ages
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        age_buckets = [0 for i in range(121)]
        for age in ages:
            age_buckets[age] += 1

        num_requests = 0

        for A in ages:
            for i in range(A, A // 2 + 7, -1):
                if i == A:
                    num_requests += age_buckets[i] - 1
                else:
                    num_requests += age_buckets[i]

        return num_requests

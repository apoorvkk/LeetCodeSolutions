'''
URL: https://leetcode.com/problems/domino-and-tromino-tiling/description/
Time complexity: O(tlogt)
Space complexity: O(s)
'''

class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache_d = [-1 for i in range(N+1)]
        cache_t = [-1 for i in range(N+1)]
        def num_tilings_d(N):
            if cache_d[N] != -1:
                return cache_d[N]
            if N <= 2:
                cache_d[N] = N
            else:
                cache_d[N] = (num_tilings_d(N-1) + num_tilings_d(N-2) + 2 * num_tilings_t(N-1)) % ((10**9) + 7)
            return cache_d[N]

        def num_tilings_t(N):
            if cache_t[N] != -1:
                return cache_t[N]
            if N <= 2:
                if N == 1:
                    cache_t[N] = 0
                else:
                    cache_t[N] = 1
            else:
                cache_t[N] = (num_tilings_d(N-2) + num_tilings_t(N-1)) % ((10**9) + 7)
            return cache_t[N]

        return num_tilings_d(N)

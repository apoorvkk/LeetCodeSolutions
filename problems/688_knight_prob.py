'''
URL: https://leetcode.com/problems/knight-probability-in-chessboard
Time complexity: O(k*n^2)
Space complexity: O(k*n^2)
'''

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        return self._aux_find_knight_prob(N, K, r, c, {})

    def _find_available_positions(self, N, r, c):
        available_positions = []
        # north section
        if r - 2 >= 0:
            if c - 1 >= 0:
                available_positions.append((r-2, c-1))

            if c + 1 < N:
                available_positions.append((r-2, c+1))

        # south section
        if r + 2 < N:
            if c - 1 >= 0:
                available_positions.append((r+2, c-1))

            if c + 1 < N:
                available_positions.append((r+2, c+1))

        # east section
        if c + 2 < N:
            if r - 1 >= 0:
                available_positions.append((r-1, c+2))

            if r + 1 < N:
                available_positions.append((r+1, c+2))

        # west section
        if c - 2 >= 0:
            if r - 1 >= 0:
                available_positions.append((r-1, c-2))

            if r + 1 < N:
                available_positions.append((r+1, c-2))

        return available_positions

    def _aux_find_knight_prob(self, N, K, r, c, probs):
        if K == 0:
            return 1.0

        if (r, c, K) in probs:
            return probs[(r, c, K)]

        available_positions = self._find_available_positions(N, r, c)
        final_probability = 0
        for i in range(len(available_positions)):
            next_pos = available_positions[i]
            next_prob = self._aux_find_knight_prob(N, K-1, next_pos[0], next_pos[1], probs)
            final_probability += 1/8.0 * next_prob

        probs[(r, c, K)] = final_probability
        return final_probability

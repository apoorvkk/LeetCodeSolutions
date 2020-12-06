'''
URL: https://leetcode.com/problems/find-the-duplicate-number/
Time complexity: O(n)
Space complexity: O(1)
'''

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):


    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        if n == 1:
            return 0

        candidate = 0
        prev_candidate = -1

        for next_person in range(1, n):
            if knows(candidate, next_person):
                prev_candidate = candidate
                candidate = next_person


        for person in range(n):
            if prev_candidate != -1 and person == prev_candidate:
                if knows(candidate, person):
                    return -1
            elif person < candidate:
                if not knows(person, candidate):
                    return -1
                if knows(candidate, person):
                    return -1
            elif person > candidate:
                if not knows(person, candidate):
                    return -1

        return candidate



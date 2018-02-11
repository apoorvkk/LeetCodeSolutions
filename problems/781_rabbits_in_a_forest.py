'''
URL: https://leetcode.com/problems/rabbits-in-forest/description/
Time complexity: O(nlogn)
Space complexity: O(1)
'''

class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if len(answers) == 0:
            return 0

        if len(answers) == 1:
            return answers[0] + 1

        answers.sort()

        group_size = answers[0]
        group_left = answers[0]
        min_rabbits = answers[0] + 1

        for i in range(1, len(answers)):
            answer = answers[i]
            if group_size == answer and group_left > 0:
                group_left -= 1
            else:
                min_rabbits += answer + 1
                group_size = answer
                group_left = answer


        return min_rabbits

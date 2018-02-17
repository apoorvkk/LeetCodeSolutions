'''
URL: https://leetcode.com/problems/asteroid-collision/description/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) == 0:
            return []

        stack = []
        for i in range(0, len(asteroids)):
            asteroid = asteroids[i]
            if len(stack) == 0:
                stack.append(asteroid)
                continue

            asteroid = asteroids[i]
            is_incoming_asteroid_dead = False

            while len(stack) > 0:
                if (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0) or (stack[-1] < 0 and asteroid > 0):
                    stack.append(asteroid)
                    break

                # Incoming asteroid will collide with our stack
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    is_incoming_asteroid_dead = True
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroid):
                    break

            if len(stack) == 0 and not is_incoming_asteroid_dead:
                stack.append(asteroid)

        return stack






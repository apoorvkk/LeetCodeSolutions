'''
URL: https://leetcode.com/problems/stamping-the-sequence
Time complexity: O(N(N-M)) where N is len of target, M is len of stamp
Space complexity: O(N(N-M))
'''

from collections import deque

class Solution:
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        visited = [False for i in range(len(target))]
        positions = []
        queue = deque()
        windows = [] # (todo, made)

        for i in range(len(target) - len(stamp) + 1):
            todo, made = set(), set()


            for j in range(i, i+len(stamp)):
                if target[j] == stamp[j-i]:
                    made.add(j)
                else:
                    todo.add(j)


            windows.append((todo, made))

            if not todo: # full stamp match
                positions.append(i)
                for j in range(i, i+len(stamp)):
                    if not visited[j]:
                        queue.append(j)
                        visited[j] = True

        while queue:
            i = queue.popleft()

            # Remove i from all todos in intersecting windows
            for j in range(max(0, i-len(stamp)+1), min(len(target)-len(stamp), i)+1):
                if i in windows[j][0]:
                    windows[j][0].remove(i)

                    if not windows[j][0]:
                        positions.append(j)
                        for k in windows[j][1]:
                            if not visited[k]:
                                queue.append(k)
                                visited[k] = True



        return positions[::-1] if all(visited) else []

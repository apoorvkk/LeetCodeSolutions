'''
URL: https://leetcode.com/problems/task-scheduler/description/
Time complexity: O(n) where n is number of tasks
Space complexity: O(26) where n is number of tasks
'''

from collections import Counter
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = Counter(tasks).values()
        heap = []

        for value in task_counts:
            heappush(heap, -value)

        total_time = 0
        tasks_left = len(tasks)
        while tasks_left > 0:
            tasks_selected = []
            i = 0
            while i <= n:
                if len(heap) > 0:
                    selected_task = -heappop(heap)
                    tasks_selected.append(selected_task)
                    tasks_left -= 1
                    total_time += 1
                elif tasks_left > 0:
                    tasks_left_in_curr_interval = n - i + 1

                    total_time += tasks_left_in_curr_interval
                    break
                else:
                    return total_time
                i +=1

            for task in tasks_selected:
                if task > 1:
                    heappush(heap, -(task - 1))

        return total_time

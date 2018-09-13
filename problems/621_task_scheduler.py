'''
URL: https://leetcode.com/problems/task-scheduler/description/
Time complexity: O(nlog(u)) where n is number of tasks and u is number of unique tasks
Space complexity: O(n) where n is number of tasks
'''

from collections import Counter
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks).values()
        heap = []

        for value in task_counts:
            heappush(heap, -value)

        total_time = 0
        tasks_completed = 0
        while len(heap) > 0:
            # Take n items out. Reduce their numbers by 1. Push them back in.
            tasks_selected = []
            for i in range(n+1):
                if len(heap) > 0: # There is a task to complete
                    selected_task = -heappop(heap)
                    tasks_selected.append(selected_task)
                    tasks_completed += 1
                    total_time += 1
                elif tasks_completed < len(tasks): # Did not finish all tasks yet so we must add more time.
                    total_time += 1


            for task in tasks_selected:
                if task > 1:
                    heappush(heap, -(task - 1))

        return total_time






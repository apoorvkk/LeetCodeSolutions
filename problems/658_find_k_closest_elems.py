'''
URL: https://leetcode.com/problems/find-k-closest-elements
Time complexity: O(logn + k)
Space complexity: O(1) <-- excludes input/output space
'''

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == 0:
            return []

        start, end = self._search(arr, x)

        return self._find_k_closest_elems(start, end, arr, x, k)

    def _find_k_closest_elems(self, start, end, arr, x, k):
        while k > 0:
            if start < 0:
                end += 1
            elif end >= len(arr):
                start -= 1
            elif abs(x - arr[start]) <= abs(x - arr[end]):
                if start == end:
                    end += 1
                start -= 1
            else:
                end += 1

            k -= 1
        return arr[max(0, start+1): min(len(arr), end)]

    def _search(self, arr, x):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == x:
                return mid, mid
            elif arr[mid] > x:
                end = mid - 1
            else:
                start = mid + 1

        return end, start

'''
URL: https://leetcode.com/problems/compare-version-numbers/description/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1s = version1.split(".")
        v2s = version2.split(".")

        for i in range(max(len(v1s), len(v2s))):

            part_v1 = int(v1s[i]) if i < len(v1s) else 0
            part_v2 = int(v2s[i]) if i < len(v2s) else 0

            if part_v1 > part_v2:
                return 1
            elif part_v1 < part_v2:
                return -1

        return 0

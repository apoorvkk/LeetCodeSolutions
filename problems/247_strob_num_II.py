'''
URL: https://leetcode.com/problems/strobogrammatic-number-ii/
'''

from collections import defaultdict

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        if n == 1:
            return ["0", "1", "8"]

        if n == 2:
            return ["11","69","88","96"]

        nums = defaultdict(list)
        nums[1].append("0")
        nums[1].append("1")
        nums[1].append("8")
        nums[2].append("00")
        nums[2].append("11")
        nums[2].append("69")
        nums[2].append("88")
        nums[2].append("96")

        self.global_n = n
        self.find_strob_nums(n, nums)
        return nums[n]


    def find_strob_nums(self, n, nums):
        if n <= 2:
            return

        available_vals = ["1", "6", "8", "9"]
        if n != self.global_n:
            available_vals.insert(0, "0")
        for val in available_vals:
            val_one = val
            val_two = val
            if val_two == "6":
                val_two = "9"
            elif val_two == "9":
                val_two = "6"

            if n-2 not in nums:
                self.find_strob_nums(n-2, nums)

            for short_num in nums[n-2]:
                nums[n].append(val_one + short_num + val_two)

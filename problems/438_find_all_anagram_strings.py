'''
URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
Time complexity: O(s)
Space complexity: O(U) where U is the unique letters in p
'''

from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s, p):
        p_counts = Counter(p)

        curr_anagram = defaultdict(int)
        unique_letters_seen = 0
        positions = []

        start = 0
        end = 0

        while end < len(s):
            curr_letter = s[end]

            # Visit the next letter
            if curr_anagram[curr_letter] < p_counts[curr_letter]: # we have found a letter to use for our curr_anagram
                curr_anagram[curr_letter] += 1
                if curr_anagram[curr_letter] == p_counts[curr_letter]:
                    unique_letters_seen += 1

            elif (curr_anagram[curr_letter] == p_counts[curr_letter]):
                if curr_letter == s[start]:
                    start += 1
                else:
                    start = end
                    end -= 1
                    unique_letters_seen = 0
                    curr_anagram = defaultdict(int)

            else: # need to reset since we have hit a delimiter
                start = end + 1
                unique_letters_seen = 0
                curr_anagram = defaultdict(int)


            # Potentially remove a letter from start
            if (end - start) + 1 == len(p):
                if unique_letters_seen == len(set(p)): #Valid anagram?
                    positions.append(start)
                curr_anagram[s[start]] -= 1
                start += 1

                unique_letters_seen -= 1


            end += 1

        return positions

'''
URL: https://leetcode.com/problems/word-break-ii
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        return self.aux_word_break(s, wordDict, {})

    def aux_word_break(self, s, word_dict, cache_segments):
        if s in cache_segments:
            return cache_segments[s]

        if len(s) == 0:
            return [""]

        all_segments = []
        for word in word_dict:
            curr_segment = word
            if s.startswith(curr_segment):
                new_segments = self.aux_word_break(s[len(curr_segment):], word_dict, cache_segments)

                for new_segment in new_segments:
                    if new_segment == "":
                        all_segments.append(curr_segment)
                    else:
                        all_segments.append(curr_segment + " " + new_segment)

        cache_segments[s] = all_segments
        return cache_segments[s]

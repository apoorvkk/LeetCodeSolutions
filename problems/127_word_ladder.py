'''
URL: https://leetcode.com/problems/word-ladder
Time complexity: O(m^2 * n)
Space complexity: O(n)
'''

from collections import deque
import string

class Solution(object):
    def _find_all_words(self, word):
        all_words = []
        for i in range(len(word)):
            for c in string.lowercase:
                all_words.append(word[:i] + c + word[i+1:])
        return all_words

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = deque()
        visited_begin = {}
        visited_end = {}

        queue.append((beginWord, True)) # (word, is_begin)
        visited_begin[beginWord] = 0

        queue.append((endWord, False))
        visited_end[endWord] = 0

        while len(queue) > 0:
            word, is_from_begin_word = queue.popleft()

            if is_from_begin_word:
                visited = visited_begin
                other_visited = visited_end
            else:
                visited = visited_end
                other_visited = visited_begin

            if word in other_visited:
                return visited[word] + other_visited[word] +1

            all_words = self._find_all_words(word) # m^2
            for potential_word in all_words: # 26m
                if potential_word in wordList and potential_word not in visited:
                    visited[potential_word] = visited[word] + 1
                    queue.append((potential_word, is_from_begin_word))

        return 0



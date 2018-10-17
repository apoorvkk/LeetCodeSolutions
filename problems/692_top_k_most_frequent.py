'''
URL: https://leetcode.com/problems/top-k-frequent-words/description/
Time complexity: O(nlogk)
Space complexity: O(n)
'''

from collections import defaultdict
from heapq import heappush, heappop

class FrequentNode:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other_frequent_node):
        if self.count == other_frequent_node.count:
            if self.word > other_frequent_node.word:
                return True
            return False
        elif self.count < other_frequent_node.count:
            return True

        return False

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = defaultdict(int)

        for word in words:
            counts[word] += 1


        heap_words = []
        for word, count in counts.iteritems():
            heappush(heap_words, FrequentNode(word, count)) # Assume minheap

            if len(heap_words) > k:
                heappop(heap_words)


        most_freq_words = []
        while len(heap_words) > 0:
            curr_node = heappop(heap_words)
            most_freq_words.append(curr_node.word)

        return most_freq_words[::-1]



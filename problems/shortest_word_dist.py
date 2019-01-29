from collections import defaultdict

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.locs = defaultdict(list)
        
        for i, word in enumerate(words):
            self.locs[word].append(i)
            
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word_one_locs = self.locs[word1]
        word_two_locs = self.locs[word2]
        
        i, j = 0, 0
        
        min_dst = float('inf')
        while i < len(word_one_locs) and j < len(word_two_locs):
            curr_word_one_loc = word_one_locs[i]
            curr_word_two_loc = word_two_locs[j]
            
            min_dst = min(min_dst, abs(curr_word_one_loc - curr_word_two_loc))
            
            if curr_word_one_loc < curr_word_two_loc:
                i += 1
            else:
                j += 1
                
        return min_dst
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
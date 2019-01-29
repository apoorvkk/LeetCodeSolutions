class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) <= 1:
            return True
        
        alien_dict = {}
        for i, l in enumerate(order):
            alien_dict[l] = i
        
        
        for i in range(1, len(words)):
            if not self._is_greater(words[i-1], words[i], alien_dict):
                return False
        
        return True
    
    def _is_greater(self, small_word, big_word, alien_dict):
        i, j = 0, 0

        while i < len(small_word) and j < len(big_word):
            if alien_dict[small_word[i]] < alien_dict[big_word[j]]:
                return True
            elif alien_dict[small_word[i]] > alien_dict[big_word[j]]:
                return False
            
            i += 1
            j += 1
        
        return len(small_word) <= len(big_word)
        
        
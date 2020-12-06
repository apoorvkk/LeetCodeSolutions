'''
URL: https://leetcode.com/problems/add-and-search-word-data-structure-design
Time complexity: O(n)
Space complexity: O(height of tree)
'''

class LetterNode:
    def __init__(self, val=None, is_last=False):
        self.val = val
        self.children = {}
        self.is_last = is_last

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = LetterNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr_node = self.root

        for i in range(len(word)):
            curr_letter = word[i]

            if curr_letter not in curr_node.children:
                curr_node.children[curr_letter] = LetterNode(curr_letter)

            curr_node = curr_node.children[curr_letter]
            if i == len(word) - 1:
                curr_node.is_last = True

    def _aux_search(self, word, curr_index, curr_node):
        if curr_index == len(word):
            return curr_node.is_last

        curr_letter = word[curr_index]

        if curr_letter == ".":
            for key, potential_node in curr_node.children.iteritems():
                found = self._aux_search(word, curr_index+1, potential_node)
                if found: return True

        elif curr_letter in curr_node.children:
            return self._aux_search(word, curr_index+1, curr_node.children[curr_letter])

        return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._aux_search(word, 0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

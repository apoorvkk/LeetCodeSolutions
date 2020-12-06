'''
URL: https://leetcode.com/problems/replace-words
Time complexity: O(max(mn, xy)) where m = num dict words, n = num letters in dict word, x = num words in sentence, y = num letters in sentence word
Space complexity: O(mn)
'''

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_root = False

class Solution:
    def replaceWords(self, roots, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root_node = self._create_trie(roots)

        def get_roots(word):
            root = self._root_found(root_node, word)
            if root:
                return root
            return word

        words = sentence.split(' ')
        root_replacements = map(get_roots, words)

        return ' '.join(root_replacements)

    def _root_found(self, root_node, word):
        curr_node = root_node

        for i, letter in enumerate(word):
            if letter not in curr_node.children:
                return None

            curr_node = curr_node.children[letter]
            if curr_node.is_root:
                return word[:i+1]
        return None

    def _create_trie(self, roots):
        root_node = TreeNode()

        for root in roots:
            curr_node = root_node
            for i, letter in enumerate(root):
                if letter not in curr_node.children:
                    curr_node.children[letter] = TreeNode(letter)

                curr_node = curr_node.children[letter]
                if i == len(root) - 1:
                    curr_node.is_root = True
        return root_node


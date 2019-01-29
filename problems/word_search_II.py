class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.final = None
        
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self._build(words)
    
    def _build(self, words):
        for word in words:
            curr_node = self.root
            for i, letter in enumerate(word):
                if letter not in curr_node.children:
                    curr_node.children[letter] = TrieNode(letter)
                curr_node = curr_node.children[letter]
            curr_node.final = word
    
    def remove_word(self, word):
        curr_node = self.root
        nodes = []
        for i, letter in enumerate(word):
            if letter not in curr_node.children: return
            curr_node = curr_node.children[letter]
            nodes.append(curr_node)
            
            if i == len(word) - 1:
                curr_node.final = None
        
        if len(nodes) == 1 and len(nodes[0].children) == 0:
            del self.root.children[nodes[0].val]
        elif len(nodes) > 0 and len(nodes[-1].children) == 0:
            for i in range(len(nodes)-2, -1, -1):
                if len(nodes[i].children) > 1: return
                
                del nodes[i].children[nodes[i+1].val]
                
class Solution(object):
    def _find_words(self, i, j, curr_node, found, board, visiting):
        if curr_node.final:
            found.append(curr_node.final)
            self.trie.remove_word(curr_node.final)
            
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = i + direction[0]
            y = j + direction[1]
            
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): continue
            if (x, y) in visiting: continue
            
            if board[x][y] in curr_node.children:
                visiting.add((x, y))
                self._find_words(x, y, curr_node.children[board[x][y]], found, board, visiting)
                visiting.remove((x, y))
            
    def findWords(self, board, words):
        self.trie = Trie(words)
        
        found = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.trie.root.children:
                    visiting = set()
                    visiting.add((i, j))
                    self._find_words(i, j, self.trie.root.children[board[i][j]], found, board, visiting)
        
        return found
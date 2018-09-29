'''
URL: Word Search Enginer
Time complexity: O(n + mlogm) where n is number of tokens and m is number of unique tokens
Space complexity: O(n)
'''

from heapq import heappush, heappop
from functools import cmp_to_key

class WordNode:
  def __init__(self, word, count, first_seen_position):
    self.word = word
    self.count = count
    self.first_seen_position = first_seen_position

def remove_punctuation(token):
  stripped_token = ""

  for char in token:
    if char.isalpha() or char.isdigit():
      stripped_token += char

  return stripped_token

def word_count_engine(document):
  tokens = document.lower().split(" ")

  word_counts = {}

  for i, token in enumerate(tokens):
    stripped_token = remove_punctuation(token)
    if stripped_token != "":
      if stripped_token in word_counts:
        word_counts[stripped_token] = (word_counts[stripped_token][0] + 1, word_counts[stripped_token][1])
      else:
        word_counts[stripped_token] = (1, i)


  word_nodes = []
  for word, value in word_counts.iteritems():
    word_nodes.append(WordNode(word, value[0], value[1]))

  def cmp(x, y):
    if x.count > y.count:
      return -1

    if x.count == y.count and x.first_seen_position < y.first_seen_position:
      return -1

    return 1

  word_nodes.sort(key=cmp_to_key(cmp))

  ordered_words = []
  for node in word_nodes:
    ordered_words.append([node.word, str(node.count)])

  return ordered_words


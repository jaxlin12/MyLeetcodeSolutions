#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
# class TrieNode:
#     def __init__(self, c=None, i=None, j=None):
#         self.c = c
#         self.i = i
#         self.j = j
#         self.next = []

# class Solution:
#     def find(self, i, j, board, words, parent):
#         if len(words) == 0:
#             return True
#         if 0 <= i < len(board) and 0 <= j < len(board[0]):
#             if board[i][j] == None:
#                 return False
#             if board[i][j] == words[0]:
#                 if parent.i == i and parent.j == j:
#                     new_node = parent
#                 else:
#                     new_node = TrieNode(board[i][j], i, j)
#                     parent.next.append(new_node)
#                     if board[parent.i][parent.j] != None:
#                         new_node.next.append(parent)
#                 temp = board[i][j]
#                 board[i][j] = None
#                 top = self.find(i-1, j, board, words[1:], new_node)
#                 if not top:
#                     down = self.find(i+1, j, board, words[1:], new_node)
#                 if not (top or down):
#                     left = self.find(i, j-1, board, words[1:], new_node)
#                 if not (top or down or left):            
#                     right = self.find(i, j+1, board, words[1:], new_node)
#                 board[i][j] = temp
#                 return top or down or left or right
#             else:
#                 return False
#         else:
#             return False

#     def checkTrie(self, node, board, words):
#         if len(words) == 0:
#             return True
#         res = False
#         if not node.next:
#             res = self.find(node.i, node.j, board, words, node)
#         else:
#             if node.i == -1 and node.j == -1:
#                 for n in node.next:
#                     res = self.checkTrie(n, board, words)
#                     if res == True:
#                         break
#             else:
#                 if len(words) == 1:
#                     return True
#                 for n in node.next:
#                     if words[1] == n.c:
#                         board[node.i][node.j] = None
#                         res = self.checkTrie(n, board, words[1:])
#                         board[node.i][node.j] = node.c
#                         if res == True:
#                             break
#                 if res != True:
#                     res = self.find(node.i, node.j, board, words, node)
#         return res

#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         ret = []
#         trieHead = []
#         for i in range(26):
#             trieHead.append(TrieNode(chr(ord('a')+i), -1, -1))
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 trieHead[ord(board[i][j]) - ord('a')].next.append(TrieNode(board[i][j], i, j))
                
#         for w in words:
#             if self.checkTrie(trieHead[ord(w[0])-ord('a')], board, w):
#                 ret.append(w)
#         return ret

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return 
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp


# @lc code=end


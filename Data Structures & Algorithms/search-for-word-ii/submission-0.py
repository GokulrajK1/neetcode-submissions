class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False 
    def add_word(self, word):
        curr = self 
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
         
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        res = set()
        visited = set()
        m, n = len(board), len(board[0])

        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or board[i][j] not in node.children:
                return 

            visited.add((i, j))
            word += board[i][j]
            curr = node.children[board[i][j]]
            if curr.is_word:
                res.add(word)

            dfs(i - 1, j, curr, word)
            dfs(i + 1, j, curr, word)
            dfs(i, j - 1, curr, word)
            dfs(i, j + 1, curr, word)

            visited.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(res)

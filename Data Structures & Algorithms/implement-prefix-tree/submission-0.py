class Node:
    def __init__(self, char, isWord = False):
        self.char = char 
        self.children = {}
        self.isWord = isWord

class PrefixTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        i = 0 
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1 

        if i == len(word):
            curr.isWord = True 
            return 

        while i < len(word):
            new_node = Node(word[i])
            curr.children[word[i]] = new_node
            curr = new_node 
            i += 1

        curr.isWord = True

    def search(self, word: str) -> bool:
        i = 0 
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1 
       
        return i == len(word) and curr.isWord

    def startsWith(self, prefix: str) -> bool:
        i = 0 
        curr = self.root
        while i < len(prefix) and prefix[i] in curr.children:
            curr = curr.children[prefix[i]]
            i += 1 
        
        return i == len(prefix)
        
        
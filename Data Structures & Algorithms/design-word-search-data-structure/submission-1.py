class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isWord = False 

class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.isWord = True

    def search(self, word: str) -> bool:

        def search_dfs(string, node):
            print("W", string)
            for i, char in enumerate(string):
                print("HI", char, node.char)
                if char not in node.children and char != ".":
                    print("End")
                    return False

                if char != ".":
                    node = node.children[char]
                    print("C")
               
                else:
                    if len(node.children) == 0:
                        print("none")
                        return False

                    for letter, child in node.children.items():
                        if search_dfs(string[i+1:], child):
                            return True 

                    return False

            return node.isWord

        return search_dfs(word, self.root)
                

        

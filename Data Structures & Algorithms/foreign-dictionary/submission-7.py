class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = {c : set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if word2.startswith(word1): continue
            if word1.startswith(word2): return ""
            for i in range(len(word1)):
                if i == len(word2): break 
                if word1[i] == word2[i]: continue 
                graph[word1[i]].add(word2[i])
                break

        stack = []
        finished = set()
        current = set()
        
        def dfs(node):

            current.add(node)

            for neighbor in graph.get(node, set()):
                
                if neighbor in current:
                   
                    return False
                if neighbor in finished:
                    continue 
                if not dfs(neighbor):
                    
                    return False 

            current.discard(node)
            finished.add(node)

            stack.append(node)

            return True

        for letter in graph.keys():
            if letter in finished: continue 

            if not dfs(letter):
                return ""

        return "".join(stack[::-1])


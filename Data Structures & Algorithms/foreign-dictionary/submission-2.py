class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        unique_chars = set()
        for word in words:
            for char in word:
                unique_chars.add(char)

        if len(words) == 1:
            return words[0][0] if len(words[0]) == 1 else ""

        graph = {c : [] for c in unique_chars}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if word2.startswith(word1):
                continue 

            if word1.startswith(word2):
                return ""
            
            for j in range(len(word1)):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    break

        order = []
        current = set()
        finished = set()
        def dfs(node):

            current.add(node)
            
            for n in graph[node]:
                if n in finished:
                    continue 
                if n in current:
                    return True 
                else:
                    if dfs(n):
                        return True
            
            order.append(node)
            current.remove(node)
            finished.add(node)
            return False 


        for char in graph:
            if char not in finished:
                
                if dfs(char):
                    return ""

        return "".join(order[::-1])



        
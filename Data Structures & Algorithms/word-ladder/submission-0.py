class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList += [beginWord]
        words = set(wordList)

        graph = {}
        for word in wordList:
            graph[word] = []

        for word in wordList:
            for i in range(len(word)):
                for x in "abcdefghijklmnopqrstuvwxyz":
                    if word[i] == x:
                        continue 
                    new_word = word[:i] + x + word[i+1:]
                    if new_word in words:
                        graph[word].append(new_word)
        
        visited = set()
        queue = deque([(beginWord, 1)])

        while queue:
            word, d = queue.popleft()
            if word in visited:
                continue 

            if word == endWord:
                return d 
            
            visited.add(word)

            for n in graph[word]:
                queue.append((n, d + 1))

        return 0 



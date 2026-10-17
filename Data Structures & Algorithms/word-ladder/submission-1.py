class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i+1:]
                graph[temp].append(word)

        visited = set([beginWord])

        queue = deque([(beginWord, 1)])

        while queue:
            word, res = queue.popleft()
            if word == endWord:
                return res 

            for i in range(len(word)):
                temp = word[:i] + "*" + word[i+1:]
                for n in graph[temp]:
                    if n in visited: continue 
                    visited.add(n)
                    queue.append((n, res + 1))

        return 0
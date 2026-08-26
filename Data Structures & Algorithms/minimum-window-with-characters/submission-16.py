class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        uniques = list(t_counts.keys())
        correct = 0
        i = 0
        s_counts = {}
        correct = 0 
        min_length = float('inf')
        res = [-1, -1]
        for j in range(len(s)):
            s_counts[s[j]] = s_counts.get(s[j], 0) + 1 
            if s[j] in t_counts and s_counts[s[j]] == t_counts[s[j]]:
                correct += 1 

            while i < j and (s[i] not in t_counts or s_counts[s[i]] > t_counts[s[i]]):
           
                s_counts[s[i]] -= 1
                i += 1 

            if correct == len(uniques):
                if j - i + 1 < min_length:
                    min_length = j - i + 1
                    res = [i, j]

            print(s_counts, correct)

        return "" if min_length == float('inf') else s[res[0]:res[1]+1]


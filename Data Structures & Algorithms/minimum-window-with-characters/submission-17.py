class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        s_counts = {}
        correct = 0
        i = 0
        n = len(s)
        res = (-1, -1)
        min_length = float('inf')
        for j in range(n):
            if s[j] not in t_counts:
                continue 
            curr = s[j]
            s_counts[curr] = s_counts.get(curr, 0) + 1
            if s_counts[curr] == t_counts[curr]:
                correct += 1 
            
            while i <= j and correct == len(t_counts):
                if s[i] not in t_counts:
                    i += 1
                    continue 
                if j - i + 1 < min_length:
                    res = (i, j)
                    min_length = j - i + 1
                s_counts[s[i]] -= 1 
                if s_counts[s[i]] < t_counts[s[i]]:
                    correct -= 1

                i += 1

        if res == (-1, -1): return ""
        return s[res[0]:res[1]+1]


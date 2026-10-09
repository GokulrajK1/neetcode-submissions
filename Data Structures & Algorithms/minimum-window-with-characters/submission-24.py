class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1 

        i = 0
        s_counts = {}
        correct = 0 
        start = -1
        length = float("inf")

        for j in range(len(s)):
            if s[j] in t_counts:
                s_counts[s[j]] = s_counts.get(s[j], 0) + 1 
                if s_counts[s[j]] == t_counts[s[j]]:
                    correct += 1 

                while i <= j and correct == len(t_counts):
                    if s[i] not in t_counts:
                        i += 1
                        continue 
                    if j - i + 1 < length:
                        length = j - i + 1
                        start = i 

                    s_counts[s[i]] -= 1
                    if s_counts[s[i]] < t_counts[s[i]]:
                        correct -= 1

                    i += 1

        if start == -1: return ""
        return s[start:start+length]


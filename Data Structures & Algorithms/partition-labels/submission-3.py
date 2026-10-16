class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, letter in enumerate(s):
            last_index[letter] = i 

        res = []

        last = 0

        i = 0

        for j in range(len(s)):
            last = max(last, last_index[s[j]])
            if last == j:
                res.append(j - i + 1)
                i = j + 1

        return res

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] in ends: 
                continue 
            ends[s[i]] = i 

        left, right = 0, 0
        end = 0
        res = []
        for right in range(len(s)):
            end = max(ends[s[right]], end)
            print(end)
            if end == right:
                print("***")
                res.append(right - left + 1)
                left = right + 1 

        return res




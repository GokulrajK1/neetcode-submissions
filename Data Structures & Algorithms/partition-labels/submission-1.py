class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1 

        l = 0
        r = 0 
        res = []
        while r < len(s):
            window = set([s[r]])
            while r < len(s) and window:
                window.add(s[r])
                counts[s[r]] -= 1 
                if counts[s[r]] == 0:
                    window.discard(s[r])
          
                r += 1 
                
            res.append(r - l)
            l = r 
          

        return res

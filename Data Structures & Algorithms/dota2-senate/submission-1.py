class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_index = deque()
        d_index = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                r_index.append(i)
            else:
                d_index.append(i)

        while r_index and d_index:
            r_i, d_i = r_index.popleft(), d_index.popleft()
            if r_i < d_i:
                r_index.append(len(senate) + r_i)
            else:
                d_index.append(len(senate) + d_i)
            
        return "Radiant" if r_index else "Dire"


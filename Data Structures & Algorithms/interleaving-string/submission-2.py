class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        def log(status, i, length, p1, p2, is1):
            mode = "IS1" if is1 else "IS2"
            print(f"{status}: i={i}, length={length}, sub={s3[i:i+length]}, p1={p1}, p2={p2}, {mode}")
        
        def backtrack(i, length, p1, p2, is1, memo):
            if (i, length, is1) in memo:
                return memo[(i, length, is1)]

            if i >= n3 and p1 >= n1 and p2 >= n2:
                return True 

            if i + length - 1 >= n3:
                return False 

            if (is1 and p1 + length - 1 >= n1) or (not is1 and p2 + length - 1 >= n2):
                return False 

            if is1:
                res = None
                if s3[i:i+length] == s1[p1:p1+length]:
                    # log("MATCH", i, length, p1, p2, is1)
                    res = backtrack(i + length, 1, p1+length, p2, False, memo) or backtrack(i, length + 1, p1, p2, True, memo)
                else:
                    # log("MISS", i, length, p1, p2, is1)
                    res = False 

                memo[(i, length, is1)] = res
                return res
            else:
                res = None
                if s3[i:i+length] == s2[p2:p2+length]:
                    # log("MATCH", i, length, p1, p2, is1)
                    res = backtrack(i + length, 1, p1, p2+length, True, memo) or backtrack(i, length + 1, p1, p2, False, memo)
                else:
                    # log("MISS", i, length, p1, p2, is1)
                    res = False 

                memo[(i, length, is1)] = res
                return res
                

        return backtrack(0, 0, 0, 0, True, {})
                


            
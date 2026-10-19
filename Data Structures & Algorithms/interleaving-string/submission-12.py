class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m, n, o = len(s1), len(s2), len(s3)

        memo = {}
        
        def backtrack(p1, p2, l, is_s1, p3):
            if (p3, l, is_s1) in memo: return memo[(p3, l, is_s1)]
            if p1 == m and p2 == n and p3 == o:
                return True 

            if p3 >= o:
                return False 

            if is_s1 and p1 + l > m:
                return False

            if not is_s1 and p2 + l > n:
                return False

            res = False

            if is_s1:
                if s1[p1:p1+l] == s3[p3:p3+l]:
                    res = res or backtrack(p1 + l, p2, 1, False, p3 + l) 

                res = res or backtrack(p1, p2, l + 1, True, p3)
            else:
                if s2[p2:p2+l] == s3[p3:p3+l]:
                    res = res or backtrack(p1, p2 + l, 1, True, p3 + l) 
                res = res or backtrack(p1, p2, l + 1, False, p3)

            memo[(p3, l, is_s1)] = res

            return res

        return backtrack(0, 0, 0, True, 0)
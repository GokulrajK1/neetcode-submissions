class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(num):

            nonlocal n, res

            if len(curr) == k:
                res.append(curr.copy())
                return

            if num > n:
                return 

            

            curr.append(num)

            backtrack(num + 1)

            curr.pop()

            backtrack(num + 1)

        backtrack(1)
        return res
            
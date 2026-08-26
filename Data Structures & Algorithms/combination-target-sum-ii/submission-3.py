class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        candidates.sort()

        def backtrack(i, total):

            if total > target:
                return 

            if total == target:
                res.append(curr.copy())
                return

            if i == len(candidates):
                return 

            curr.append(candidates[i])

            print(curr)

            backtrack(i + 1, total + candidates[i])

            curr.pop()

            j = i
            while j + 1 < len(candidates) and candidates[j + 1] == candidates[j]:
                j += 1

            backtrack(j + 1, total)

        backtrack(0, 0)
        return res
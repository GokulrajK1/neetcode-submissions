class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            best = float("-inf")
            take = 0
            for k in range(3):
                if i + k >= n: break 
                take += stoneValue[i + k]
                best = max(best, take - dp[i + k + 1])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
                

        # memo = {}
        
        # def backtrack(i, is_alice):

        #     if (i, is_alice) in memo: return memo[(i, is_alice)]

        #     if i >= n: return (0, 0)

        #     stone1, stone2, stone3 = stoneValue[i], stoneValue[i + 1] if i + 1 < n else 0, stoneValue[i + 2] if i + 2 < n else 0

        #     take_1_alice, take_1_bob = backtrack(i + 1, not is_alice)
        #     take_2_alice, take_2_bob = backtrack(i + 2, not is_alice)
        #     take_3_alice, take_3_bob = backtrack(i + 3, not is_alice)

        #     res = None

        #     if is_alice:
        #         TAKE_3_ALICE = take_3_alice + stone1 + stone2 + stone3
        #         TAKE_2_ALICE = take_2_alice + stone1 + stone2 
        #         TAKE_1_ALICE = take_1_alice + stone1 
        #         max_alice = max(TAKE_3_ALICE, TAKE_2_ALICE, TAKE_1_ALICE)

        #         if TAKE_3_ALICE == max_alice:
        #             res = (TAKE_3_ALICE, take_3_bob)
        #         elif TAKE_2_ALICE == max_alice:
        #             res = (TAKE_2_ALICE, take_2_bob)
        #         else:
        #             res = (TAKE_1_ALICE, take_1_bob)
        #     else:
        #         TAKE_3_BOB = take_3_bob + stone1 + stone2 + stone3
        #         TAKE_2_BOB = take_2_bob + stone1 + stone2 
        #         TAKE_1_BOB = take_1_bob + stone1 
        #         max_bob = max(TAKE_3_BOB, TAKE_2_BOB, TAKE_1_BOB)

        #         if TAKE_3_BOB == max_bob:
        #             res = (take_3_alice, TAKE_3_BOB)
        #         elif TAKE_2_BOB == max_bob:
        #             res = (take_2_alice, TAKE_2_BOB)
        #         else:
        #             res = (take_1_alice, TAKE_1_BOB)

        #     memo[(i, is_alice)] = res

        #     return res

        # alice_score, bob_score = backtrack(0, True)
        # if alice_score > bob_score:
        #     return "Alice"
        # elif bob_score > alice_score:
        #     return "Bob"
        # else:
        #     return "Tie"

            



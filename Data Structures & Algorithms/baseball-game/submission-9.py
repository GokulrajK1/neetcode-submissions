class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "+":
                score1, score2 = scores[-1], scores[-2]
                scores.append(score1 + score2)
            elif operation == "D":
                score = scores[-1]
                scores.append(score * 2)
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation)) 

        return sum(scores)
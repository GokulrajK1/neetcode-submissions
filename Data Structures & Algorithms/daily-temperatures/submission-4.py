class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                index, temp = stack.pop()
                res[index] = i - index 

            stack.append((i, temperatures[i]))

        return res

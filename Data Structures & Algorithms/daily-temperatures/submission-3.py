class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                _, j = stack.pop()
                res[j] = i - j 

            stack.append((temperature, i))

        return res 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = []
        values = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while values and values[-1] < temperature:
                res[index[-1]] = i - index[-1]
                index.pop()
                values.pop()
            values.append(temperature)
            index.append(i)

        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        indicies = []
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while temps and temps[-1] < temperature:
                index = indicies.pop()
                res[index] = i - index 
                temps.pop()
            temps.append(temperature)
            indicies.append(i)

        return res
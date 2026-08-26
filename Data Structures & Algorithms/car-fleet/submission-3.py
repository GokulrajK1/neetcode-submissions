class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(pos, (target - pos) / vel) for pos, vel in zip(position, speed)]
        times.sort(key=lambda x: x[0], reverse=True)
        print(times)
        stack = []
        for time in times:
            stack.append(time)
            while len(stack) > 1 and stack[-2][1] >= stack[-1][1]:
                stack.pop()

        print(stack)

        return len(stack)
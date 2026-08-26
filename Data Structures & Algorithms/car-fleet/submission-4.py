class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(pos, (target - pos) / vel) for pos, vel in zip(position, speed)]
        times.sort(key=lambda x : x[0])
        stack = []
        for time in times:
            while stack and stack[-1][1] <= time[1]:
                stack.pop()
            stack.append(time)
    
        return len(stack)
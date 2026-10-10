class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vehicles = [(pos, (target - pos) / v) for pos, v in zip(position, speed)]
        vehicles.sort()
        stack = []
   
        for pos, time in vehicles:
            while stack and stack[-1] <= time:
                prev_time = stack.pop()
            
            stack.append(time)

        return len(stack)

            
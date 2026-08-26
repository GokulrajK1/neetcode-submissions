class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort(key = lambda x : x[0])
        for car in cars:
            time = (target - car[0]) / car[1]

            while stack and stack[-1] <= time:
                stack.pop() 

            stack.append(time)

        return len(stack)
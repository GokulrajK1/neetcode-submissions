class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(pos, (target - pos) / speed) for pos, speed in zip(position, speed)]
        cars.sort(key = lambda x : x[0])
        for car in cars:
            while stack and stack[-1][1] <= car[1]:
                prev_car = stack.pop() 

            stack.append(car)

        return len(stack)
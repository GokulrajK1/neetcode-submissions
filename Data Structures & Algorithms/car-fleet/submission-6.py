class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, (target - pos) / vel) for pos, vel in zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse=True)
        stack = []
        for car in cars: 
            stack.append(car)
            while len(stack) > 1 and stack[-1][1] <= stack[-2][1]:
                car1, car2 = stack.pop(), stack.pop()
                stack.append((car2[0], car2[1]))

            print(stack)

        return len(stack)

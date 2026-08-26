class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and (stack[-1] <= 0 and stack[-2] >= 0):
                a1, a2 = stack.pop(), stack.pop()
                if abs(a1) == abs(a2):
                    continue
                if abs(a1) > abs(a2):
                    stack.append(a1)
                else:
                    stack.append(a2)

        return stack
            
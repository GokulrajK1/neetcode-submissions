class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            should_add_to_stack = True
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    should_add_to_stack = False 
                    break 
                else:
                    should_add_to_stack = False
                    break 
            if should_add_to_stack:
                stack.append(asteroid) 

        return stack
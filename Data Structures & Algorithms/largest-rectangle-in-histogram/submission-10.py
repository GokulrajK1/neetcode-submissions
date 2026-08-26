class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        for h in heights:
            
            stack.append((h, 1))
            min_height = float("inf")
            count = 0
            while len(stack) > 1 and stack[-1][0] <= stack[-2][0]:
                h1, h2 = stack.pop(), stack.pop()
                max_area = max(max_area, h2[0] * h2[1])
                min_height = min(min_height, h2[0])
                count += h2[1]
                stack.append((h1[0], h1[1] + h2[1]))
            
                max_area = max(max_area, (min_height if min_height != float("inf") else 0) * count)
            max_area = max(max_area, (min_height if min_height != float("inf") else 0) * count)

        prev_c = 0
        print(stack)
        while stack:
            h, c = stack.pop()
            prev_c += c 
            max_area = max(max_area, h * prev_c)
           
        return max_area

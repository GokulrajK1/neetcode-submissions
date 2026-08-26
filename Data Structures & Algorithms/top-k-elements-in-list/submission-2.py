class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        max_count = -1
        for num in nums:
            count_num = counts.get(num, 0) + 1
            counts[num] = count_num
            if count_num > max_count:
                max_count = count_num 

        print(max_count)
        
        elements = [[] for i in range(max_count + 1)]
        print(elements)
        for element, count in counts.items():
            print(count)
            elements[count].append(element)
        
        most_frequent = []
        for element_list in elements[::-1]:
            if len(element_list) > 0:
                most_frequent += element_list
                if len(most_frequent) == k:
                    return most_frequent

        
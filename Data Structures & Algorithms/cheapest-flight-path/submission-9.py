class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = {x : float("inf") for x in range(n)}
        dist[src] = 0 
        for _ in range(k + 1):
            d = dist.copy()
            for from_i, to_i, price_i in flights:
                if d[to_i] > dist[from_i] + price_i:
                    d[to_i] = dist[from_i] + price_i

            dist = d

        return dist[dst] if dist[dst] != float("inf") else - 1

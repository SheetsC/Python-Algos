import heapq

class Solution:
    def getLargest(self, k: int, arr):
        if k <= 0 or not arr:
            return None
        sort_heap = []
        for element in arr:
            heapq.heappush(sort_heap, element)
            if len(sort_heap) > k:
                heapq.heappop(sort_heap)
        return sort_heap[0]


solution = Solution()
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(solution.getLargest(k, arr))  

               

        
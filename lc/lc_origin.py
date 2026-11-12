import math
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        #you want closest point so u need to throw largest out, maxheap
        maxheap=[]
        for point in points:
            x = point[0]
            y = point[1]
            dist = - math.sqrt((x**2) + (y**2))
            print(dist, point)
            heapq.heappush(maxheap,(dist, point))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        #top = heapq.heappop(maxheap) #only1
        #result = [top[1]]
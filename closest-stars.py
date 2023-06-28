# this is a problem given by skilledInc and has grading criteria
# efficient solution, good use of data structures, 
# complete solution, and define a custom obj
# it is recommended to use a heap to store stars as they are sorted
import heapq

class Star:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def findNearestStar(self, stars, k):
        if isinstance(k, int):
            nearest_stars = []
            for star in stars                                                                                                                                                                :
                distance = star.distance
                heapq.heappush(nearest_stars, (distance, star))
                if len(nearest_stars) > k:
                    heapq.heappop(nearest_stars)
            
            nearest_distances = [star[0] for star in nearest_stars]
            return nearest_distances
class Star:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    
    def findNearestStar(self, stars, k):
        if isinstance(k, int):
            stars.sort(key=lambda star: star.distance)
            sorted_distances = [star.distance for star in stars]
            nearest_distances = sorted_distances[:k]
            return nearest_distances

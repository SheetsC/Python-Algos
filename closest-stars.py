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

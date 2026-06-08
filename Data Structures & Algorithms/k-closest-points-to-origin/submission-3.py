import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x,y = point[0], point[1]
            distance = (0 - x)**2 + (0 - y)**2
            distances.append([distance, point])
        distances.sort()
        final = distances
        for i in range(len(final)):
            final[i] = final[i][1]
        return final[:k]
    
    def sortDistances(self, distances: List[List[int]], s, e) -> List[List[int]]:
        length = e - s
        if length <= 1:
            return distances
        pivot = e - 1
        left = s
        for i in range(s,e):
            distance = distances[i][0]
            if distance > distances[pivot][0]:
                temp = distances[pivot]
                distances[pivot] = distances[i]
                distances[left] = temp
                left += 1
        self.sortDistances(distances, s, left - 1)
        self.sortDistances(distances, left + 1, e)
        return distances


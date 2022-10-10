from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        # TODO-0: скопируйте реализацию из предыдущей задачи
        return ((self.x - other_point.x) ** 2 +  (self.y - other_point.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

ncoor = Point(0, 0)
dist = []

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты

for point in points:
    print(point.dist_to(ncoor))
    dist.append(point.dist_to(ncoor))
    

print("Coordinates: ", max(dist))

from __future__ import annotations
from math import sin, cos, sqrt, atan2, radians

R = 6371


class Coordinate():
    def __init__(self, lattitude, longitude):
        self.lattitude_deg = lattitude
        self.lattitude_rad = radians(lattitude)
        self.longitude_deg = longitude
        self.longitude_rad = radians(longitude)

    def distance(self, coordinate: Coordinate):
        dlat = coordinate.lattitude_rad - self.lattitude_rad
        dlon = coordinate.longitude_rad - self.longitude_rad

        a = sin(dlat / 2)**2 + cos(self.lattitude_rad) * cos(coordinate.lattitude_rad) * sin(dlon / 2)**2

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance


if __name__ == "__main__":
    coord_France = Coordinate(46.23, 2.21)
    coord_Japon = Coordinate(36.2, 138.25)
    coord_Grèce = Coordinate(39.07, 21.82)

    print(coord_France.distance(coord_Japon))
    print(coord_France.distance(coord_Grèce))

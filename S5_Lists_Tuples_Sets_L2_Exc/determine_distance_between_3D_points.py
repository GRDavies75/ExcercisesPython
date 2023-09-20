"""
Excercise 5-27
Determine the distance between two 3D-points
The coordinates are represented by lists [x, y, z]
The calculation can be done:
AB = Square root of ((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2 ) 

You may assume there are always a list of 3 numbers
you always return a float
"""
import math as m


def calculate_distance_between_two_3d_points(
        pointA: list[float],
        pointB: list[float]) -> float:
    """
    Points are represented by a 3 numbered list [x, y, z]
    
    return m.sqrt( (B.x - A.x) ** 2 + (B.y - A.y) ** 2 + (B.z - A.z) ** 2)
    """
    Ax, Ay, Az = pointA
    Bx, By, Bz = pointB

    # Debugging
    # tmp = m.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2 + (Bz - Az) ** 2)
    # print(pointA, pointB, tmp)

    return m.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2 + (Bz - Az) ** 2)


def main() -> None:
    input_data = [
        ([1,2,3], [1,2,3]),
        ([3,4,5], [1,3,5]),
        ([-3,4,-5], [2,0,-4]),
    ]

    for point1, point2 in input_data:
        print(calculate_distance_between_two_3d_points(point1, point2))


if __name__ == "__main__":
    main()

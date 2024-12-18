import random
import math

def random_points_on_unit_circle(num_points):
    points = []
    for _ in range(num_points):
        angle = random.uniform(0, 2 * math.pi)
        x = math.cos(angle)
        y = math.sin(angle)
        points.append((x, y))
    return points

def is_acute_triangle(points):
    (x1, y1), (x2, y2), (x3, y3) = points

    angle1 = math.atan2(y2 - y1, x2 - x1)
    angle2 = math.atan2(y3 - y2, x3 - x2)
    angle3 = math.atan2(y1 - y3, x1 - x3)

    return angle1 < math.pi/2 and angle2 < math.pi/2 and angle3 < math.pi/2

def simulation(num):
    count_acute_triangles = 0
    for _ in range(num):
        points = random_points_on_unit_circle(3)
        if is_acute_triangle(points):
            count_acute_triangles += 1

    probability = count_acute_triangles / num
    return probability

num_sims = 1000000
print("The probability that the triangle defined by these points as vertices has three acute angles is:", simulation(num_sims))

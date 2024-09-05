import math

# Constants
increment = 0.1
starting_point = [1, 1]
point1 = [1, 5]
point2 = [6, 4]
point3 = [5, 2]
point4 = [2, 1]

# Distance calculation
def distance(x1, y1, x2, y2):
    return math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)

# Sum of distances from one point to all others
def sum_of_distances(x1, y1, points):
    total_distance = 0
    for px, py in points:
        total_distance += distance(x1, y1, px, py)
    return total_distance

# Calculate the new distance for a moved point
def new_distance(x1, y1, points):
    total_distance = sum_of_distances(x1, y1, points)
    return [x1, y1, total_distance]

# Determine the point corresponding to the minimum distance
def get_new_point(minimum, d1, d2, d3, d4):
    if d1[2] == minimum:
        return [d1[0], d1[1]]
    elif d2[2] == minimum:
        return [d2[0], d2[1]]
    elif d3[2] == minimum:
        return [d3[0], d3[1]]
    elif d4[2] == minimum:
        return [d4[0], d4[1]]

# List of points to compare with
points = [point1, point2, point3, point4]

# Initial sum of distances
min_distance = sum_of_distances(starting_point[0], starting_point[1], points)
flag = True
i = 1

# Optimization loop
while flag:
    # Calculate distances for new possible points
    d1 = new_distance(starting_point[0] + increment, starting_point[1], points)
    d2 = new_distance(starting_point[0] - increment, starting_point[1], points)
    d3 = new_distance(starting_point[0], starting_point[1] + increment, points)
    d4 = new_distance(starting_point[0], starting_point[1] - increment, points)
    
    # Print the current iteration and point
    print(i, round(starting_point[0], 2), round(starting_point[1], 2))
    
    # Find the minimum distance
    minimum = min(d1[2], d2[2], d3[2], d4[2])
    
    # If a better point is found, update the starting point
    if minimum < min_distance:
        starting_point = get_new_point(minimum, d1, d2, d3, d4)
        min_distance = minimum
        i += 1
    else:
        flag = False

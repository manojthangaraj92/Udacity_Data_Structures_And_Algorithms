from math import sqrt
from queue import PriorityQueue

def generate_path(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path

# For this particular problem, euclidean distance is chosen as the heuristic function. 
# Euclidean distance is the straight line distance between the two coordinates. 

# There are some other types of distances could be considered, such as Manhattan, which is inspired from the manhattan city in
# new york from reaching one point to the other in city will be like moving in the perfect squares. It is a distance between two points 
# measured along axes at right angles.

# The manhattan distance would be calculated from the formula,  h = abs (current_cell.x – goal.x) + abs (current_cell.y – goal.y)

# Manhattan distance would only be suitable when we are allowed to move in four directions (right, left, top, bottom).

# The next distance would be the Diagonal distance measurement, Now this is a measurement of either the vertical distance on y axis or the horizontal distance on x-axis. 
# This tells us about the tru distance like in pythogorous theorem. This is used when it is allowed to move on all 8 directions.

# The diagonal distance would be calculated from the formula, 

#dx = abs(current_cell.x – goal.x)
#dy = abs(current_cell.y – goal.y)
#h = D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
#where D is length of each node(usually = 1) and D2 is diagonal distance between each node (usually = sqrt(2)). 

# The diagonal distance would be useful when we are allowed to move in eight direction only (similar to move of aking in chess).

# The A* algorithm is informed search and we need to move in any directions as we want to find the shortest route possible, the right heuristic function would be 
# Euclidean distance.

def euclidean_distance(start, goal):
    distance = sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))
    return distance

def shortest_path(M,start,goal):
    path = PriorityQueue()
    path.put(start, 0)

    prev = {start: None}
    value = {start: 0}

    while not path.empty():
        current = path.get()
        if current == goal:
            generate_path(prev, start, goal)

        for node in M.roads[current]:
            updated_score = value[current] + euclidean_distance(
                M.intersections[current],
                M.intersections[node]
            )

            if node not in value or updated_score < value[node]:
                value[node] = updated_score
                total_score = updated_score + euclidean_distance(
                    M.intersections[current], M.intersections[node])
                path.put(node, total_score)
                prev[node] = current

    return generate_path(prev, start, goal)


# References

# https://github.com/python/cpython/blob/85c128e34daec7625b74746e127afa25888ccde1/Lib/queue.py#L223 --> Priority Queue
# https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/a-star-algorithm#how_to_implement_the_a_algorithm_in_python 
# https://www.geeksforgeeks.org/a-search-algorithm/
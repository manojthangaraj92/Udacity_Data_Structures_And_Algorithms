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

# Since the map loaded here was a straight between the nodes, choosing Euclidean would be the best option.

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
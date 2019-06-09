'''
A M by N matrix consisting of booleans that representing
a board where each True boolean represents a wall and each
False boolean represents a tile you can walk on. Given
this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end
coordinate from the start. If there is no possible path, then
return null. You can move up, left, down, and right. You
cannot move through walls. You cannot wrap around the edges
of the board.

For e.g. if the board input is [[f,f,f,f],
                                [t,t,f,t],
                                [f,f,f,f],
                                [f,f,f,f]]
If the object has to move from (3,0) to (0,0), then the
code should return 7.
'''

import numpy as np

# Function returning the distance between the current point
# and the goal location
def dist(point1, point2):
    return pow((pow(point1[0] - point2[0],2)) + (pow(point1[1] - point2[1], 2)), 0.5)

# Function returning the list of possible traversable options
def edges(point, board, n_r, n_c):

    # available points to move
    edge_list = []

    temp_list = [(point[0]+1, point[1]),
                 (point[0]-1, point[1]),
                 (point[0], point[1]+1),
                 (point[0], point[1]-1)]

    for var in temp_list:
        if var[0] >= 0 and var[0] < n_r and var[1] >=0 and var[1] < n_c:
            if board[var[0]][var[1]] == False:
                edge_list.append(var)

    return edge_list

# Counting the steps taken to reach from start to goal
def count_steps(dict_pt, start, end):
    count = 0
    curr_pt = end

    while curr_pt != start:
        count += 1
        curr_pt = dict_pt.get(curr_pt)

    return count

# Function returning the minimum num of steps required to
# move from start to end point
def retd_steps(board, start, end, n_r, n_c):

    # Point dictionary, storing the parent point of each point
    dict_pt = {}

    # Initializing the open_list containing the un-travelled points
    # closed_list containing the travelled points, g_cost containing
    # the edge cost and f_cost containing the value to reach the goal
    open_list, closed_list = [start], []
    f_cost = np.full([n_r, n_c], np.inf, dtype = float)
    g_cost = np.full([n_r, n_c], np.inf, dtype = float)

    g_cost[start[0]][start[1]] = 0
    f_cost[start[0]][start[1]] = g_cost[start[0]][start[1]] + dist(start, end)

    # Running the loop till the open_list is not empty
    while open_list is not None:

        if not open_list:
            return "Path not found"

        # Selecting the point with minimum f_cost
        temp_pt = open_list[0]

        for var in open_list:
            if f_cost[var[0]][var[1]] < f_cost[temp_pt[0]][temp_pt[1]]:
                temp_pt = var

        curr_pt = temp_pt

        # Ending the loop if goal is found
        if curr_pt == end:
            return count_steps(dict_pt, start, end)

        closed_list.append(curr_pt)
        open_list.remove(curr_pt)
        curr_edges = edges(curr_pt, board, n_r, n_c)

        # Updating the edge costs of the neighboring nodes
        for var in curr_edges:
            if var in closed_list:
                continue

            temp_g_cost = g_cost[curr_pt[0]][curr_pt[1]] + dist(var, curr_pt)

            if var not in open_list:
                open_list.append(var)
            elif temp_g_cost >= g_cost[var[0]][var[1]]:
                continue

            # Updating f_cost, g_cost and saving the parent to the neighbor pt
            dict_pt[var] = curr_pt
            g_cost[var[0]][var[1]] = temp_g_cost
            f_cost[var[0]][var[1]] = g_cost[var[0]][var[1]] + dist(var, end)


#Taking the input from the user for board, start and goal
n_r, n_c = 4, 4
board = np.full([n_r, n_c], False, dtype = bool)

# defining the wall obstacles
obs_list = [(1,0),(1,1),(1,2),(1,3)]
for var in obs_list:
    board[var[0]][var[1]] = True

# start and end point
start, end = (3,0), (0,0)
print(retd_steps(board, start, end, n_r, n_c))

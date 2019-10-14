# Find the available point for the object to traverse. The verification will depend
# on the availability of the grid location, whether it is empty or has some obstacle
def find_edge(curr_var, grid, num_rows, num_cols, obstacle_dict, is_sword):
    
    # possible directions for traversing, Up/Down/Left/Right
    possible_edges = [(curr_var[0] + 1, curr_var[1]),
                        (curr_var[0], curr_var[1] - 1),
                        (curr_var[0] - 1, curr_var[1]),
                        (curr_var[0], curr_var[1] + 1)]
    
    edges = []

    # To check if a sword is available for the input grid defined by the user
    # If yes, then only walls will be represented as obstacles. If not, then
    # both dragon and walls will be represented as obstacles.
    if not is_sword:
        temp_list = []
        temp_list.extend(obstacle_dict['walls'])
        temp_list.extend(obstacle_dict['dragon'])
    
    for var in possible_edges:
        if var[0] >= 0 and var[0] < num_rows and var[1] >= 0 and var[1] < num_cols:
            if is_sword and var not in obstacle_dict['walls']:
                edges.append(var)
            elif not is_sword and var not in temp_list:
                    edges.append(var)
                
    
    return edges
    
# Return the shortest path cost. The path cost will be the total path cost of
# individual paths, if there are multiple positions for the robot to visit
def shortest_path(grid, start, goal, sword, treasure):

    # Initialize the lists to store the open and visted locations
    closed_list  = []  
    dict_cost = {}
    open_list = [start]

    # Calculate the rows and columns of the input grid
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    dict_cost[start] = 0

    # dictionary to store the set of obstacles
    obstacle_dict = {'walls': [(1, 1), (1, 2), (2, 2), (2,3)],
                        'dragon': [(0,2)]}
                            
    curr_cost = 0;
    
    # adding the goal coord to treasure list as well
    treasure.append(goal)
    goal_list = []

    # To update the goal list if there is sword available, and append the
    # treasure locations to the list
    if sword:
        goal_list.extend(sword)
        goal_list.extend(treasure)
        is_sword = True
    else:
        is_sword = False
        goal_list.extend(treasure)
        
    curr_goal = goal_list[0]

    # Iterate till the open list is not empty
    while open_list:
        curr_var = open_list[0]
        
        # to check if the goal is found or not
        if curr_var == curr_goal:
            
            # adding the cost for each individual path (A to B) + (B to C)
            curr_cost += dict_cost[curr_var]
            goal_list.remove(curr_goal)
            
            # to check if the goal list(treasure) is not empty
            if not goal_list:
                print("path found")
                return curr_cost
            else:
                # emptying the dictionary for cost, so that previous cost values
                # doesn't affect the new path costs
                dict_cost = {}
                dict_cost[curr_var] = 0
                closed_list = []
                open_list = [curr_var]
                curr_goal = goal_list[0]
            
        open_list.remove(curr_var)
        closed_list.append(curr_var)
        
        edges = find_edge(curr_var, grid, num_rows, num_cols, obstacle_dict, is_sword)

        # Iterate over the valid list of edges to be stored in open list
        for var in edges:
            if var in closed_list:
                continue
            
            if var not in open_list:
                open_list.append(var)
            
            if var not in dict_cost.keys():
                dict_cost[var] = dict_cost[curr_var] + 1
            elif dict_cost[var] > dict_cost[curr_var] + 1:
                dict_cost[var] = dict_cost[curr_var] + 1
        
    # if no path exists then print path not found 
    print("path not found")
    
    return 0


# Take the input grid defined by the user, where '@', '.', '#', 'W',
# '$' and 't' represents start, open location, wall, dragon, treasure
# and sword respectively. The aim is to visit and collect all the possible
# treasure locations as defined by the user
grid = [['@', '.', 'W', '.'], 
       ['.', '#', '#', '$'], 
       ['.', 'X', '#', '#'], 
       ['.', '.', '$', 't']]
     
start = (0,0)
goal = (2,1) 
sword = [(3,3)]
treasure = [(3,2)]      # could be multiple locations as well
print("Total path cost", shortest_path(grid, start, goal, sword, treasure))
    

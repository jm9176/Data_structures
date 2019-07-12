'''
Ordering the package dependencies
'''
# Function to return the order in which the packages will
# be completed
def pack_order(inp_map):

    # List storing the nodes which have not been traversed
    # completely and closed_list to store the nodes which have
    # been fully visited
    open_list = []
    closed_list = []

    # Funcion to traverse the neighboring nodes
    # and updating the open and closed list accordingly
    def node_neigh(node):

        if node in closed_list:
            return

        open_list.append(node)

        # to check if the node is in the neighboring nodes
        # but not available in the map keys
        if node in inp_map.keys():

            # traversing the corresponding neighboring nodes
            for var in inp_map[node]:

                # to check if the graph has a cycle
                if var in open_list:
                    raise Exception('graph has a cycle')

                if var not in closed_list:
                    node_neigh(var)

        else:
            raise Exception('Node not found')

        # updating the open and closed list
        open_list.remove(node)
        closed_list.append(node)

    # traversing the map keys
    for var in inp_map.keys():
        node_neigh(var)

    return 'The package order is: {}'.format(closed_list)


# Taking the package dependency input
pack_map = {'A':['B','C'],
            'B':['D'],
            'C':['B'],
            'D':[]}

print(pack_order(pack_map))

def roadsAndLibraries(n, c_lib, c_road, cities):
    def dfs(s):
        global visited, alist, valCount
        visited[s] = 1;
        l = len(alist[s]);
        valCount += 1
        if (l != 0):
            for i in xrange(l):
                if (visited[alist[s][i]] == 0): dfs(alist[s][i])

    q = int(raw_input().strip())
    valCount = 0
    for a0 in xrange(q):
        n, m, clib, croad = map(int, raw_input().split())
        visited = [0 for i in xrange(n + 1)];
        alist = [[] for i in xrange(n + 1)]
        count = 0;
        roads = 0;
        road = [];
        current = 0
        for a1 in xrange(m):
            city_1, city_2 = map(int, raw_input().split(' '))
            alist[city_1].append(city_2);
            alist[city_2].append(city_1)
        if (m == 0 or croad >= clib):
            print n * clib
        else:
            for i in xrange(1, n + 1):
                if (visited[i] == 0):
                    valCount = 0
                    dfs(i)
                    road.append(valCount)
            ans = 0;
            p = len(road)
            for i in xrange(p): ans += min((road[i] - 1) * croad + clib, road[i] * clib)
            print ans

#-------------------------------------------------------------

def dfs(s):
    global visited,alist,valCount,croad,cost
    visited[s]=1;l=len(alist[s]);valCount+=1
    if(l!=0):
        for i in xrange(l):
            if(visited[alist[s][i]]==0):
                dfs(alist[s][i])
                cost+=croad
q = int(raw_input().strip())
valCount=0
for a0 in xrange(q):
    cost=0
    n,m,clib,croad=map(int,raw_input().split())
    visited=[0 for i in xrange(n+1)];alist=[[] for i in xrange(n+1)]
    count=0;roads=0;road=[];current=0
    for a1 in xrange(m):
        city_1, city_2 = map(int,raw_input().split(' '))
        alist[city_1].append(city_2);alist[city_2].append(city_1)
    if(m==0 or croad>=clib): print n*clib
    else:
        for i in xrange(1,n+1):
            if(visited[i]==0):
                valCount=0
                dfs(i)
                cost+=clib
        print cost


#--------------------------------------------------------------
import sys

q = int(input().strip())
for a0 in range(q):
    # every query starting from scrach
    sets_flat = {}
    labels = {}
    val_map = {}
    result = 0
    cnt = 0

    a = input()
    n_cities, n_roads, cost_lib, cost_road = a.strip().split(' ')
    n_cities, n_roads, cost_lib, cost_road = [int(n_cities), int(n_roads), int(cost_lib), int(cost_road)]

    if n_roads == 0:
        print(n_cities * cost_lib)
        continue

    if cost_lib < cost_road:
        print(cost_lib * n_cities)

        # ingest and pass remaining inputs
        for a1 in range(n_roads):
            input()
        continue

    for a1 in range(n_roads):
        cnt += 1

        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]

        c1_label = sets_flat.get(city_1, None)
        c2_label = sets_flat.get(city_2, None)

        if (not c1_label) and (not c2_label):
            label = 'set_{}'.format(cnt)
            val = 'val_{}'.format(cnt)
            labels[label] = val

            sets_flat[city_1] = label
            sets_flat[city_2] = label

            val_map[val] = [label]

        elif (c1_label) and (not c2_label):
            sets_flat[city_2] = c1_label

        elif (not c1_label) and (c2_label):
            sets_flat[city_1] = c2_label

        elif labels[c1_label] == labels[c2_label]:
            continue

        elif labels[c1_label] != labels[c2_label]:
            val_map[labels[c1_label]].extend(val_map[labels[c2_label]])
            val_map.pop(labels[c2_label])

            for label in val_map[labels[c1_label]]:
                labels[label] = labels[c1_label]

        result += cost_road  # +1 road

    # count libraries from merged sets
    result += (len(set(labels.values()))) * cost_lib

    # add separated cities
    count_cities_in_sets = len(sets_flat)
    if count_cities_in_sets < n_cities:
        result += (cost_lib * (n_cities - count_cities_in_sets))

    print(result)

#-------------------------------------------------------------------------

roads = 0
def dfsUtil(node, visited, g):
    global roads
    visited[node] = True

    for i in g[node]:
        if visited[i] == False:
            roads += 1
            dfsUtil(i, visited, g)

def dfs(g, lib):
    visited = {}
    v = len(g)
    for i in g:
        visited[i] = False

    for j in g:
        if visited[j] == False:
            lib += 1
            dfsUtil(j, visited, g)
    return roads, lib

q = int(input().strip())
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    ways = {}
    roads = 0
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        if city_1 not in ways:
            ways[city_1] = []
        if city_2 not in ways:
            ways[city_2] = []
        ways[city_1].append(city_2)
        ways[city_2].append(city_1)
    r, l = dfs(ways, 0)
    clr = r * y + l * x
    cl = len(ways) * x
    low=min(clr,cl)
    rest=n-len(ways)
    print((rest*x)+low)

#------------------------------------------------------------
#probar este primero

import sys

def Explore(city):
    global cost
    c = roads[city]
    for j in c:
        if cities[j] != 1:
            cities[j] = 1
            cost += y
            Explore(j)
q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    a = n+1
    roads = [[] for i in range(n+1)]
    cities = [0]*a
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        roads[city_1].append(city_2)
        roads[city_2].append(city_1)
    cost = 0
    if x < y:
        print(x*n)
        continue
    for i in range(1,a):
        if cities[i]!=1:
            cities[i] = 1
            cost += x
            Explore(i)
    print(cost)


#-------------------------------------------------------------

class UnionFind(object):

    def __init__(self, n):
        self.arr = [-1 for x in range(n+1)]

    def find(self, x):
        # find
        start = x
        while (self.arr[x] >= 0):
            x = self.arr[x]
        # path compression
        root = x
        x = start
        while (self.arr[x] >= 0):
            start = self.arr[x]
            self.arr[x] = root
            x = start
        return root

    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        # tree (i) has less elements then (j)
        if self.arr[i] > self.arr[j]:
            self.arr[j] += self.arr[i]
            self.arr[i] = j
        else:
            self.arr[i] += self.arr[i]
            self.arr[j] = i


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n*c_lib
    # algorythm find:union
    uf = UnionFind(n)
    nbLibraries = n
    nbRoads = 0
    for c1, c2 in cities:
        if(uf.find(c1) != uf.find(c2)):
            uf.union (c1, c2)
            nbRoads += 1
            nbLibraries -= 1
    return (nbRoads * c_road + nbLibraries * c_lib)


#----------------------------------------------
import sys


class Kingdom(object):
    def __init__(self):
        self.connections = {}
        self.library_access = {}

    def add_city(self, city):
        self.connections[city] = []
        self.library_access[city] = False

    def add_connection(self, city1, city2):
        self.connections[city1].append(city2)
        self.connections[city2].append(city1)

    def buy_roads(self, cost_r, cities):
        cost = 0
        for city in cities:
            if not self.library_access[city]:
                # print('road for', city, 'at', cost_r, '$')
                self.library_access[city] = True
                cost += cost_r
                cost += self.buy_roads(cost_r, self.connections[city])
        return cost

    def buy_library(self, cost_l, city):
        cost = 0
        if not self.library_access[city]:
            # print('library for', city, 'at', cost_l, '$')
            self.library_access[city] = True
            cost += cost_l
        return cost

    def solve(self, cost_l, cost_r):
        cost = 0
        for city, connections in self.connections.items():
            cost += self.buy_library(cost_l, city)
            if cost_l > cost_r:
                cost += self.buy_roads(cost_r, connections)
        return cost


q = int(input().strip())
for a0 in range(q):
    kingdom = Kingdom()
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = int(n), int(m), int(x), int(y)
    for i in range(n):
        kingdom.add_city(i + 1)
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        kingdom.add_connection(city_1, city_2)

    print(kingdom.solve(x, y))


#----------------------------------------------------------

class Graph(object):
    """Class undirected graph"""
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_nodes_from(self, nodes):
        """Adds nodes from a list"""
        for node in nodes:
            self.nodes.add(node)
            self.edges[node] = []

    def add_edges_from(self, edges):
        """Add edges from a list of tuples"""
        for edge in edges:
            # Only add the edge if the node is previously in the graph
            if edge[0] in self.nodes and edge[1] in self.nodes:
                # Undirected edges (bidirectional)
                self.edges[edge[0]].append(edge[1])
                self.edges[edge[1]].append(edge[0])

    def get_children_of_node(self, node):
        return self.edges[node]

    def get_connected_component_subgraphs_nodes(self):
        """
        We use a set of unvisited nodes and start BFS searches choosing an arbitrary node.
        We count all the nodes in each subgraph so we can calculate the minimal cost later.
        ITS FUNDAMENTAL to use a set to represent the unvisited nodes so checking and deleting a node is O(1)

        Returns:
            list_number_nodes_subgraphs: A list of the number of nodes of the subgraphs the graph contains.
            Ex: [45, 325, 1232, 1]
        """
        # Set of still unvisited nodes
        unvisited_nodes = self.nodes.copy()
        # List of ints representing the amount of nodes in each subgraph
        list_number_nodes_subgraphs = []
        while len(unvisited_nodes) > 0:
            # Start counting how many nodes will be in this subgraph
            subgraph_nodes = 0
            # Get new arbitrary parent, and add it back to the set
            # (there's no way to get an element without eliminating it in a set)
            root_node = unvisited_nodes.pop()
            unvisited_nodes.add(root_node)
            # Implement BFS and find all connected nodes to parent
            queue = [root_node]
            while len(queue) > 0:
                current_node = queue.pop(0)
                subgraph_nodes += 1
                unvisited_nodes.remove(current_node)
                for children in self.get_children_of_node(current_node):
                    # Avoid visiting a node more than once
                    if (children in unvisited_nodes) and (children not in queue):
                        queue.append(children)
            list_number_nodes_subgraphs.append(subgraph_nodes)
        return list_number_nodes_subgraphs


def build_graph(query):
    """Instances a graph and adds nodes and edges to it"""
    g = Graph()
    g.add_nodes_from(query["cities"])
    g.add_edges_from(query["roads"])
    return g


def calculate_minimal_price_subgraph(n_nodes, c_lib, c_road):
    """
    Calculates the minimal price for a subgraph using the number of nodes it has
    1 case: Expensive roads --> Just build a library in each city
    2 case: Expensive library --> Build one library and connect all the cities with roads

    Args:
        n_nodes: Number of nodes of the subgraph
        c_lib: Cost of building a library
        c_road: Cost of building a road

    Returns:
        Int of the minimal cost for this subgraph
    """
    if c_road > c_lib:
        return c_lib * n_nodes
    else:
        return c_lib + c_road * (n_nodes-1)


def calculate_minimal_price_graph(n_nodes_subgraphs, c_lib, c_road):
    """
    Works like a greedy algorithm getting the total minimal price
    as the sum of the minimal prices of all the subgraphs

    Args:
        n_nodes_subgraphs: List of the number of nodes of each subgraph
        c_lib: Cost of building a library
        c_road: Cost of building a road

    Returns:
        Int total minimal cost
    """
    total_cost = 0
    for n_nodes in n_nodes_subgraphs:
        total_cost += calculate_minimal_price_subgraph(n_nodes, c_lib, c_road)
    return total_cost



def get_input_from_prompt():
    """ Reads all the queries and stores the info in a list of queries"""
    # First line is the number of queries
    n_queries = int(input())
    queries = []
    for __query in range(n_queries):
        # For each query get the number of cities, roads and the cost of each one
        n_cities, n_roads, c_lib, c_road = [int(x) for x in input().split()]
        # Create the cities list
        cities = [city for city in range(1, n_cities+1)]
        # Create the roads list
        roads = []
        for __road in range(n_roads):
            roads.append(tuple(map(int, input().split())))
        # Append the new query
        queries.append({"n_cities": n_cities, "n_roads": n_roads, "c_lib": c_lib, "c_road": c_road,
                        "cities": cities, "roads": roads})
    return queries


def main():
    my_queries = get_input_from_prompt()
    for my_query in my_queries:
        a_graph = build_graph(my_query)
        n_nodes_subgraphs = a_graph.get_connected_component_subgraphs_nodes()
        minimal_price = calculate_minimal_price_graph(n_nodes_subgraphs, my_query["c_lib"], my_query["c_road"])
        print(minimal_price)


if __name__ == "__main__":
    main()
#---------------------------------------------------------------
#works perfect
import sys
from collections import deque
q = int(input().strip())
for a0 in range(q):
    count = 0
    citySet = set()
    n, m, cityLibCost, cityRoadCost = input().strip().split(' ')
    n, m, cityLibCost, cityRoadCost = [int(n), int(m), int(cityLibCost), int(cityRoadCost)]
    cityGraph = {k : [] for k in range(n+1)}
    citySet = set()
    totalCities = n
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        cityGraph[city_1] += [city_2]
        cityGraph[city_2] += [city_1]
        citySet.add(city_1)
        citySet.add(city_2)
    Discovered = set()
    queueBFS = deque() #append() append right, popleft() pop from left side
    no_of_connected_components = 0
    citiesInConnectedComponents = list()
    for city in citySet:
        if city not in Discovered:
            Discovered.add(city)
            queueBFS.append(city)
        noOfCities = 0
        while queueBFS:
            city_node = queueBFS.popleft()
            noOfCities += 1
            for adjCity in cityGraph[city_node]:
                if adjCity not in Discovered:
                    queueBFS.append(adjCity)
                    Discovered.add(adjCity)
        if noOfCities > 0:
            citiesInConnectedComponents += [noOfCities]
    totalCost = 0
    no_of_connected_cities = len(citySet)
    if cityLibCost < cityRoadCost:
        totalCost = cityLibCost * totalCities
    elif cityLibCost > cityRoadCost:
        for n in citiesInConnectedComponents:
            totalCost += cityRoadCost * (n-1) + cityLibCost
        if totalCities > len(citySet):
            diff = totalCities - no_of_connected_cities
            totalCost += cityLibCost * diff
    else:
        totalCost = cityLibCost * no_of_cities
    print(totalCost)


#--------------------------------------------------------
class Graph:
    """ Adjacency-list graph. """
    def __init__(self, nnodes):
        self.nodes = {index: [] for index in range(nnodes)}
        self.nnodes = nnodes

    def add_edge(self, x, y):
        self.nodes[x].append(y)
        self.nodes[y].append(x)


def count_road_cities(graph):
    """
    Does DFS on a graph, returns the count of edges in the MST, and the number of components.

    Based on Skiena's implementation of edge-classification on undirected graphs.
    All edges are either tree-edges or back edges, we only care about tree edges
    here.
    """
    tree_edge_count = 0
    discovered = [False] * graph.nnodes
    component_count = 0

    def recurse(node_index):
        nonlocal tree_edge_count
        discovered[node_index] = True
        for edge in graph.nodes[node_index]:
            if not discovered[edge]:
                discovered[edge] = True
                tree_edge_count += 1
                recurse(edge)

    for node_index in graph.nodes:
        if not discovered[node_index]:
            component_count += 1
            recurse(node_index)
    return tree_edge_count, component_count

q = int(input().strip())
for a0 in range(q):
    nnodes, nedges, library_cost, road_cost = input().strip().split(' ')
    nnodes, nedges, library_cost, road_cost = [int(nnodes,), int(nedges,), int(library_cost,), int(road_cost)]
    if library_cost < road_cost:
        print(nnodes * library_cost)
        # Just burn through the information about the edges, we don't care about it
        # and just want to advance to the next query.
        for _ in range(nedges):
            input()
    else:
        graph = Graph(nnodes=nnodes)
        for _ in range(nedges):
            city_1, city_2 = input().strip().split(' ')
            # One-indexing!!!
            graph.add_edge(int(city_1) - 1, int(city_2) - 1)
        roads, cities = count_road_cities(graph)
        print(roads * road_cost + cities * library_cost)

#-----------------------------------
import sys
q = int(input().strip())
w = 0
for a0 in range(q):
    n, m, c_lib, c_road = input().split(' ')
    n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
    if c_lib <= c_road or m == 0:
        print(n*c_lib)
    else:
        v_flag = [0 for c in range(n+1)]
        cost , v_count = 0 , 0
        for a1 in range(m):
            city_1, city_2 = input().split(' ')
            city_1, city_2 = [int(city_1), int(city_2)]
            if (v_flag[city_1] == 0  )and (v_flag[city_2 ] == 0):
                v_count += 2
                v_flag[city_1] = 1
                v_flag[city_2] = 1
                cost += c_lib
                cost += c_road
            elif (v_flag[city_1] == 1 )and (v_flag[city_2] == 1):
                    w = 1
            else:
                cost+=c_road
                if v_flag[city_1] == 0 :
                    v_count += 1
                    v_flag[city_1] = 1
                else:
                    v_count += 1
                    v_flag[city_2] = 1
        if v_count == n:
            print(cost)
        else:
            cost += (n - v_count)*c_lib
            print(cost)

#-----------------------------
#Non recursive implementation
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]

    adjList = [[] for i in range(n + 1)]
    # build adjacency list
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        adjList[city_1].append(city_2)
        adjList[city_2].append(city_1)

    if m == 0 or x <= y:
        print(x * n)
        continue

    cost = 0
    stack = []
    visited = [0 for i in range(n + 1)]
    # loop through all cities to ensure we see all components
    for city in range(1, n + 1):
        if visited[city] != 0:
            continue

        cost += x
        stack.append(city)
        # non recursive DFS
        while stack:
            currentCity = stack.pop()
            for adjCity in adjList[currentCity]:
                if visited[adjCity] == 0:
                    stack.append(adjCity)
                    visited[adjCity] = 1
                    cost += y

            visited[currentCity] = 2
    print(cost)
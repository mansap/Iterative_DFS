import sys


# SearchGraph.py
#
# Implementation of iterative deepening search for use in finding optimal routes
# between locations in a graph. In the graph to be searched, nodes have names
# (e.g. city names for a map).
#
# An undirected graph is passed in as a text file (first command line argument).
#
# Usage: python SearchGraph.py graphFile startLocation endLocation
#
# Author: Richard Zanibbi, RIT, Nov. 2011
#         Mansa Pabbaraju

# global variables used to store information relating to search space
result = False
val = False
visited = []
path = []
tree = ''
cost = {}

def read_graph(filename):
	"""Read in edges of a graph represented one per line,
	using the format: srcStateName destStateName"""
	print("Loading graph: " + filename)
	edges = {}

	inFile = open(filename)
	for line in inFile:
		roadInfo = line.split()

		# Skip blank lines, read in contents from non-empty lines.
		if (len(roadInfo) > 0):
			srcCity = roadInfo[0]
			destCity = roadInfo[1]

			if srcCity in edges:
				edges[srcCity] = edges[srcCity] + [destCity ]
			else:
				edges[srcCity] = [ destCity ]

			if destCity in edges:
				edges[destCity] = edges[destCity] + [ srcCity ]
			else:
				edges[destCity] = [ srcCity ]

	print("  done.\n")
	print ('Edges:',edges)
	return edges

######################################
# Add functions for search, output
# etc. here
######################################

# TBD

#########################
# Main program
#########################
def main():
	if len(sys.argv) != 4:
		print('Usage: python SearchGraph.py graphFilename startNode goalNode')
		return
	else:
		# Create a dictionary (i.e. associative array, implemented as a hash
		# table) for edges in the map file, and define start and end states for
		# the search. Each dictionary entry key is a string for a location,
		# associated with a list of strings for the adjacent states (cities) in
		# the state space.
		edges = {}
		edges = read_graph(sys.argv[1])
		start = sys.argv[2]
		goal = sys.argv[3]

		# Comment out the following lines to hide the graph description.
		# print("-- Adjacent Cities (Edge Dictionary Data) ------------------------")
		# for location in edges.keys():
		# 	s = '  ' + location + ':\n     '
		# 	s = s + str(edges[location])
		# 	print(s)

		if not start in edges.keys():
			print("Start location is not in the graph.")
		else:
			StartSearch(start,edges,goal)

# Function Name:
#          StartSearch()
# Input parameters:
#          start - start location
#          edges - map of Romania
#          goal - goal location
# Working:
#          This function takes in the start
#          and goal location along with the map of Romania
#          as input parameters and begins the IDS starting from depth 0.
#          This function calls the DFS function iteratively from depth 0 until
#          any of the following conditions occur:
#          1. The goal state has been found
#          2. All states have been visited and goal state is not found. This is 'Failure'.
#          It also prints the search tree traversed in each iteration of the IDS when the maximum depth for
#          the current iteration of IDS has been reached.
# Return values: None

def StartSearch(start,edges,goal):
	global result
	global val
	global tree
	global path,visited
	list = []
	depth = -1
	res_list = []
	while val == False and result == False:
		depth = depth + 1
		res_list = DFS(start,edges,goal,list,depth,-1)
		print()
		print('Tree at depth: ',depth)
		print(tree)
		tree = ''
		#clear 'visited' list for every max depth iteration of IDS.
		visited = []

	if (result == True):
		print('\n')
		print('Done, path found of length = ',depth)
		print('\n' + 'The path is as follows: ')
		print(res_list)
	else:
			print(res_list)

# Function Name:
#          DFS()
# Input parameters:
#          node - state from which this instance of DFS needs to start
#          edges - all cities in map of Romania
#          dest - goal location, remains constant throughout all iterations of IDFS
#          list - local list which keeps track of all nodes visited in this iteration of IDFS
#          depth - the maximum depth value of this iteration
#          d - current depth in this instance of iteration
# Working:
#          This is the recursive DFS which runs for iterations of 'depth' value.
#          The current depth level always is -1 initially. It begins iteration from level 0 to the depth level.
#          This iterative DFS loop is run until any one of the following 3 conditions are satisfied:
#          1. The goal state is reached in the most optimal way
#          2. All states have been checked, yet the goal has not been discovered.
#             This means that the goal state does not exist.
#          3. The maximum depth level has been reached.
# Return values:
#          A list containing the following:
#          1. If the goal state has been reached, it returns a list of cities in th path to
#          reach goal in the most optimum way.
#          2. If the goal is not found, it returns a list with string 'Failure'.
#

# d is always -1 initially
def DFS(node,edges,dest,list, depth,d):
	global result,val,visited,tree,path,cost
	d = d + 1
	list = list + [node]
	tree =  tree + '\t ' * d + node + '\n'
	if node not in visited:
		visited = visited + [node]
	cost[node] = d

	if(node == dest) or (len(edges) == len(visited)) or (d == depth):
		if len(edges) == len(visited):
			val = True
			path = ['Failure']
		if (node == dest):
			path = list
			result = True
			val = True
		return path

	else:
		ret_list = []
		for next in edges[node]:
			#if a longer path found for this iteration of IDS itself,
			# do not pursue it.
				if next in visited and cost[next] < d+1:
					continue
				elif next not in list and result == False:
					ret_list = DFS(next,edges,dest,list,depth,d)
					#if all nodes are visited return 'Failure' or return path
					if len(path) > 1:
						break
		return ret_list

# Execute the main program.
main()


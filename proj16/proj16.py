# Name:
# Date:
#
# proj16
#
# Graph optimization
# Finding shortest paths through campus buildings
#

import string
from graph import *


#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph)
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    f = open(mapFilename, 'r')
    graph = weightedDigraph()
    for line in f:
        data = line.split()
        src = data[0]
        dest = data[1]
        tot = int(data[2])
        out = int(data[3])
        if not graph.hasNode(src):
            graph.addNode(src)
        if not graph.hasNode(dest):
            graph.addNode(dest)
        graph.addWeightedEdge(weightedEdge(src, dest, tot, out))
    return graph


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    return bruteForceSearchRec(digraph, start, end, maxTotalDist,
                                      maxDistOutdoors)



def bruteForceSearchRec(digraph, start, end, maxTotalDist, maxDistOutdoors,
                        visited = [], totalDist = 0, outDist = 0,
                        path = [], path_list = []):


    edge_list = digraph.childrenOf(start)

    for edge in edge_list:

        if edge in visited:
            continue

        else:
            checkDist = totalDist + edge[1]
            checkOutDist = outDist + edge[2]

            if checkDist < maxTotalDist and checkOutDist < maxDistOutdoors:
                visited.append(edge)
                path.append(edge)


                if edge[0] == end:
                    path_list.append(path)
                    break

                else:
                    bruteForceSearchRec(digraph, edge[0], end, maxTotalDist,
                                        maxDistOutdoors,
                                        visited, checkDist, checkOutDist, path)

                    #path = path[:-1]

            else:
                continue
        #path = path[:-1]


    #if path[-1][0] == end:
        #path_list.append(path)

    path = path[:-1]


    print path












    # visited.append(edge)
    # totalDist += edge[1]
    # outDist += edge[2]
    # print "Visiting: " + str(edge) + ", totalDist = " + str(totalDist) + ", outDist = " +\
    #                                str(outDist)
    #
    #
    # if totalDist > maxTotalDist or outDist > maxDistOutdoors:
    #     return None
    # elif edge in visited:
    #     return None
    # else:
    #     path.append(edge)
    #     if edge[0] == end:
    #         return path
    #     else:
    #         edge_list = digraph.childrenOf(edge[0])
    #         for edge in edge_list:
    #             path = [edge] + bruteForceSearchRec(digraph, edge, end, maxTotalDist,
    #                             maxDistOutdoors, totalDist, outDist, path, visited)






#     #print "options: " + str(digraph.childrenOf(cur))
#     visited.append(cur)
#     cur_path.append(cur)
#
#     edge_list = digraph.childrenOf(cur)
#     #if cur == start:
#         #print edge_list
# #
#     for edge in edge_list:
#
#         #if cur == start:
#             #print edge
#         #print str(edge)
#         #print "visited: " + str(visited)
#         #print "cur_path: " + str(cur_path)
#
#
#         dest = edge[0]
#         tot = edge[1]
#         out = edge[2]
#
#         #print "dest: " + str(dest),
#
#         if dest in visited:
#             #print "visited"
#             continue
#
#         elif (tot + totalDist) > maxTotalDist or (out + outDist) > maxDistOutdoors:
#             #print "too far"
#             continue
#
#         elif dest == end:
#             #print "end, ",
#             cur_path.append(dest)
#             paths.append(cur_path)
#             #print str(cur_path)
#             #print "PATHS: " + str(paths)
#             cur_path = cur_path[:-1]
#             tots.append(totalDist + tot)
#             outs.append(outDist + out)
#             #print "stats: " + str(cur_path) + ", " + str(totalDist + tot) + ", " + str(
#                 #outDist + out)
#
#
#
#             #print "break on edge_list: " + str(edge_list) + ", cur = " + str(cur), ", " \
# #"dest = " + str(dest)
#             break
#
#         else:
#             #print "NOT end, "
#             totalDist += tot
#             outDist += out
#             #print "stats: " + str(cur_path) + ", " + str(totalDist) + ", " + str(
#                 #outDist)
#
#             bruteForceSearchRec(digraph, start, dest, end, maxTotalDist,
#                                 maxDistOutdoors, tots, outs, totalDist, outDist,
#                                 visited, cur_path, paths)
#
#             cur_path = cur_path[:-1]
#             #totalDist -= tot
#             #outDist -= out
#         cur_path = cur_path[:-2]
#         visited = visited[:-1]
#         #totalDist -= tot
#         #outDist -= out
#     #cur_path = cur_path[:-1]
#
#
#
#
#
#     #print paths










    # #visited.append(cur)
    #
    # path = [cur]
    #
    # if cur == start:
    #     totalDist = 0
    #     outDist = 0
    #
    # if cur == end:
    #     bestTot = totalDist
    #     bestOut = outDist
    #     return path
    #
    # best_path = None
    #
    # for edge in digraph.childrenOf(cur):
    #     dest = edge[0]
    #     tot = edge[1]
    #     out = edge[2]
    #
    #     if dest not in visited:
    #
    #         withTot = totalDist + tot
    #         withOut = outDist + out
    #         better = False
    #
    #         if withTot < bestTot:
    #             better = True
    #         elif withTot == bestTot and withOut <= bestOut:
    #             better = True
    #         if better:
    #             visited.append(dest)
    #             newPath = bruteForceSearchRec(digraph, start, dest, end, bestTot,
    #                                            bestOut,
    #                                       withTot, withOut, visited, best_path)
    #
    #             if newPath != None:
    #                 if best_path == None:
    #                     best_path = newPath
    #
    #
    #
    # if best_path:
    #     path = path + best_path
    # else:
    #     path = None
    #
    # return path







    #print "Current Building: " + cur
    #print "Edges to Try :" + str(digraph.childrenOf(cur))

    # for edge in digraph.childrenOf(cur):
    #     #print "trying building: " + edge[0]
    #
    #     dest = edge[0]
    #     tot = edge[1]
    #     out = edge[2]
    #
    #     if dest == end:
    #         #print "This is the end."
    #         best = False
    #         if totalDist + tot < bestTot:
    #             best = True
    #         elif totalDist + tot == bestTot and outDist + out < bestOut:
    #             best = True
    #         if best:
    #             #print "This is the best path."
    #             path = [dest]
    #             bestTot = totalDist + tot
    #             bestOut = outDist + out
    #             continue
    #         else:
    #             #print "This is a path, but not the best path."
    #             path = None
    #
    #     elif dest in visited:
    #         #print "This is the start."
    #         continue
    #
    #     else:
    #         #print "This is not the start or the end."
    #         if totalDist + tot <= bestTot and outDist + out <= \
    #                 bestOut:
    #             totalDist += tot
    #             outDist += out
    #             try:
    #                 bruteForceSearchRec(digraph, dest, end, bestTot, bestOut,
    #                                        totalDist,
    #                                    outDist, visited, path, best_path)
    #                 if path != None:
    #
    #                 [cur] + best_path
    #             except:
    #                 totalDist -= tot
    #                 outDist -= out
    #                 continue
    #
    #
    #
    # if best_path:
    #     return best_path
    # else:
    #     raise ValueError("No path satisfies the constraints")


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    # TODO
    pass


# Uncomment below when ready to test
if __name__ == '__main__':
    # Test cases
    digraph = load_map("campus_map.txt")

    LARGE_DIST = 1000000

    # Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
##
    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
##
    # Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
##
    # Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
##
    # Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
##
    # Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
##
    # Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
##
    # Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

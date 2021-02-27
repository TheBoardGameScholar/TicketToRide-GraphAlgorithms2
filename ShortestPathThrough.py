# Class for finding the shortest path through specific nodes for Ticket To Ride Graph Algorithm Project
# Board Game Scholar Post 2
# Freddy Reiber

from City import City
from Route import Route
from USABoard import setUpUSABoard
from TicketToRide import *

import copy

listOfCites = setUpUSABoard()


# Finds gets all of the Routes for a specific board
def getAllRoutes(cityList):
    allRoutes = []
    for city in cityList:
        routes = city.getRoutes()
        for route in routes:
            allRoutes.append(route)
    return allRoutes


# Floyd–Warshall algorithm
def findAllShortestPaths(cityList):
    routes = getAllRoutes(cityList)
    rows, cols = (len(cityList), len(cityList))

    # This generates nested arrays for easy indexing
    dist = dict()
    for city in cityList:
        dist[city.getName()] = dict()
        for city2 in cityList:
            dist[city.getName()][city2.getName()] = 100

    next = dict()
    for city in cityList:
        next[city.getName()] = dict()
        for city2 in cityList:
            next[city.getName()][city2.getName()] = None

    for route in routes:
        dist[route.city1][route.city2] = route.cost
        dist[route.city2][route.city1] = route.cost
        next[route.city1][route.city2] = route.city2
        next[route.city2][route.city1] = route.city1
    for city in cityList:
        dist[city.name][city.name] = 0
        next[city.name][city.name] = 0
    for k in cityList:
        for i in cityList:
            for j in cityList:
                if dist[i.name][j.name] > dist[i.name][k.name] + dist[k.name][j.name]:
                    dist[i.name][j.name] = dist[i.name][k.name] + dist[k.name][j.name]
                    next[i.name][j.name] = next[i.name][k.name]

    return dist, next


def findPath(next, u, v):
    if next[u][v] == None:
        return []
    path = [u]
    while u != v:
        u = next[u][v]
        path.append(u)
    return path


def createdTSP(dist, next, listOfNodes):
    newGraph = []
    for startingNode in listOfNodes:
        newCity = City(startingNode)
        for destinationNode in listOfNodes:
            if startingNode == destinationNode:
                continue
            newCity.addRoute(Route(startingNode, destinationNode, dist[startingNode][destinationNode]))
        newGraph.append(newCity)
    pathDict = {}
    for city in listOfNodes:
        pathDict[city] = {}
        for city2 in listOfNodes:
            if city2 == city:
                continue
            pathDict[city][city2] = findPath(next, city, city2)

    return newGraph, pathDict


def cityIsAvailable(citys, route):
    for city in citys:
        if city.name == route.city2:
            return True
    return False


def findCity(cityGraph, city):
    for possibleCity in cityGraph:
        if possibleCity.name == city:
            cityGraph.remove(possibleCity)
            return possibleCity
    return None


# Global variables for this function. Unfortunately, Python doesn't have any static variables :/
bestPath = None
currentSmallest = 1000
currentOrder = []


# Uses a brute force algorithm to try all permutations
def solveTSP(cityGraph, nextCity):
    # This function is used to find all possible combinations, since we need to brute force here
    # This is somewhat messy because of how I have chosen to abstract the graph.
    global bestPath
    global currentSmallest
    global currentOrder

    if len(cityGraph) == 1:
        counter = 0
        for route in currentOrder:
            counter += route.cost
        if counter < currentSmallest:
            currentSmallest = counter
            bestPath = copy.deepcopy(currentOrder)
    elif nextCity is None:
        for city in cityGraph:
            cityGraph.remove(city)
            for route in city.getRoutes():
                currentOrder.append(route)
                solveTSP(cityGraph, route.city2)
                currentOrder.pop()
            cityGraph.append(city)
    else:
        nextCity = findCity(cityGraph, nextCity)
        for route in nextCity.getRoutes():
            if cityIsAvailable(cityGraph, route):
                currentOrder.append(route)
                solveTSP(cityGraph, route.city2)
                currentOrder.pop()
        cityGraph.append(nextCity)


def findShortestPathThroughNodes(cityGraph, listOfCities):
    dist, path = findAllShortestPaths(cityGraph)
    tspGraph, pathDict = createdTSP(dist, path, listOfCities)
    solveTSP(tspGraph, None)
    masterRoute = []
    for route in bestPath:
        toAppend = pathDict[route.city1][route.city2]
        for item in toAppend[:-1]:
            masterRoute.append(item)
    masterRoute.append(bestPath[-1].city2)

    return masterRoute


def main():
    print("Input which cities you would like to find the shortest path through! Use Finished to move on")
    cityList = []
    while True:
        newInput = input()
        if newInput == "Finished":
            break
        cityList.append(newInput)
    print(findShortestPathThroughNodes(listOfCites, cityList))


main()

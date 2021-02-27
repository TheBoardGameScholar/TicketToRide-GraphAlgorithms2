# Main class for Ticket To Ride Graph Algorithm Project
# Board Game Scholar Post 2
# Freddy Reiber

from City import City
from Route import Route
from USABoard import setUpUSABoard
from ShortestPathThrough import *

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


# Uses Dijkstra's algorithm to find the shortest path between two cities.
def findShortestPath(map, city1, city2):
    # Sets initial values
    # Current set of unexplored Cities
    citySet = []
    # Shortest distance for X city to city1/source node
    distance = {}
    # The previous node we visit to find this node through its shortest path
    previous = {}
    for city in map:
        distance[city.getName()] = 1000
        previous[city.getName()] = None
        citySet.append(city)
    distance[city1] = 0

    # Main Loop
    while len(citySet) != 0:
        # Searches citySet for the city with the least distance[u] value
        u = citySet[0]
        for city in citySet:
            if distance[city.getName()] <= distance[u.getName()]:
                u = city

        # Removes city from set of unexplored nodes as we are exploring it now
        citySet.remove(u)

        # Added since we only care about finding the shortest path to city2, not all nodes
        if u.getName() == city2:
            break

        # Updates all nodes currently not explored
        possibleDestinations = u.getAllDestinations()
        for destination in possibleDestinations:
            altRoute = distance[u.getName()] + destination[1]
            if altRoute < distance[destination[0]]:
                distance[destination[0]] = altRoute
                previous[destination[0]] = u.getName()

    # Using a trace back through previous we can get the reverse from city1 to city2
    pathToCity = []
    u = city2
    while u is not None:
        pathToCity.append(u)
        u = previous[u]
    # Reverse the path
    pathToCity.reverse()

    # We can just return the distance to city2 as distance is a measurement of the shortest path from city1 to x node
    return distance[city2], pathToCity


def main():
    city1 = input("Enter starting city")
    city2 = input("Enter ending city")
    x, y = findShortestPath(listOfCites, city1, city2)
    print("Shortest path from start to end:")
    for station in y:
        print("  -" + station)
    print("Total cost for the trip: " + str(x))


main()

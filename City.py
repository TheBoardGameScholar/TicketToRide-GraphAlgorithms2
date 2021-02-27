# City Class for Ticket to Ride Algorithms Project
# This Class Models each City on a Ticket to Ride Boar
# This class is basically a Node in Graph Theory!
# Board Game Scholar Post 2
# Freddy Reiber

import Route


class City:

    # Class init requires the Cities name and a list of all Routes that touch it.
    def __init__(self, nameOfCity, listOfRoutes=None):
        if listOfRoutes is None:
            listOfRoutes = list()
        self.name = nameOfCity
        self.routes = listOfRoutes

    def __repr__(self):
        return self.name

    # Getters
    def getName(self):
        return self.name

    def getRoutes(self):
        return self.routes

    # Gets all possible Destinations with cost, returned in a list of tuples
    def getAllDestinations(self):
        allDestinations = []
        for route in self.routes:
            if route.getCity1() != self.name:
                destination = route.getCity1()
            else:
                destination = route.getCity2()
            cost = route.getCost()
            allDestinations.append((destination, cost))
        return allDestinations

    # Setters
    def addRoute(self, newRoute):
        self.routes.append(newRoute)

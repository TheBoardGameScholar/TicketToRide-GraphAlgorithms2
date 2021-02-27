#Main class for Ticket to Ride Graph Algorithms
#This class models each route on a Ticket to Ride Map
#This class is modeled after Edges in Graph Theory
##Board Game Scholar Post 2
#Freddy Reiber

class Route:

    #Constructor
    def __init__(self, city1, city2, cost, color = "Grey"):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost
        self.color = color

    def __repr__(self):
        return self.city1 + " -> " + self.city2 + "(" + str(self.cost) + ")"

    #Getters
    def getCost(self):
        return self.cost

    def getCity1(self):
        return self.city1

    def getCity2(self):
        return self.city2

    def getColor(self):
        return self.color


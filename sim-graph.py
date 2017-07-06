import random
import pylab

class Location(object):
    # Creates location object with x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Updates a location object by adding an x dist and y dist
    def move(self, deltx, delty):
        return Location(self.x + deltx, self.y + delty)
    # Returns X of location
    def getX(self):
        return self.x
    # Returns Y of location
    def getY(self):
        return self.y
    # Calculates distance between self and another location object
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<' + str(self.x) + ", " + str(self.y) + '>'

class Person(object):
    # Creates a person by storing a name
    def __init__(self, name):
        self.name = name
    # Chooses a direction to move
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)
    def __str__(self):
        return "This person is named " + self.name

class Field(object):
    # Creates a field object represented by a dictionary of people
    def __init__(self):
        self.people = {}
    # If person not in people dict, add the person and their location to the people dict
    def addPerson(self, person, loc):
        if person in self.people:
            raise ValueError('duplicate')
        else:
            self.people[person] = loc
    # Updates the location of a person
    def movePerson(self, person):
        if not person in self.people:
            raise ValueError("Person not in field")
        xDist, yDist = person.takeStep()
        self.people[person] = self.people[person].move(xDist, yDist)
    # Returns the location of a person
    def getLoc(self, person):
        if not person in self.people:
            raise ValueError("Person not in field")
        return self.people[person]

# Moves a person a certain number of steps in a field
def walk(field, person, numSteps):
    start = field.getLoc(person)
    for step in range(numSteps):
        field.movePerson(person)
    return(start.distFrom(field.getLoc(person)))

# Simulates a walk through a field
# Walk is length numSteps
# Runs numTrial simulations
def simWalks(numSteps, numTrials):
    walker = Person('Walker')
    origin = Location(0,0)
    distances = []

    for trial in range(numTrials):
        field = Field()
        field.addPerson(walker, origin)
        distances.append(walk(field, walker, numSteps))

    return distances

def randomWalkTest(numTrials):
    stepList = [10, 100, 1000, 10000, 100000]
    meanDistance = []
    maxDistance = []
    minDistance = []
    for numSteps in stepList:

        distances = simWalks(numSteps, numTrials)
        print "Random walk of " + str(numSteps) + ' steps'
        mean = sum(distances)/len(distances)
        meanDistance.append(mean)
        maximum = max(distances)
        maxDistance.append(maximum)
        minimum = min(distances)
        minDistance.append(minimum)
        print 'Mean Distance = ', mean
        print 'Max  Distance = ', maximum, 'Min Distance = ', minimum

    pylab.plot(stepList, meanDistance)
    pylab.plot(stepList, maxDistance)
    pylab.plot(stepList, minDistance)
    pylab.legend(("Mean Distance", "Max Distance", "Min Distance" ))
    pylab.title("Distance from origin over 10 - 100000 steps")
    pylab.xlabel("Step Number")
    pylab.ylabel("Distance from origin")
    #pylab.legend()
    pylab.show()

randomWalkTest(100)




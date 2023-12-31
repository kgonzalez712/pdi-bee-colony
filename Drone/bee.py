import random

class BeeDrone():
    def __init__( self,initialDirection, initialX, initialY): 
        self.direction = initialDirection
        self.positionX = initialX
        self.positionY = initialY
        self.northValue = 0
        self.southValue = 0
        self.eastValue = 0
        self.westValue = 0
        self.northCellQuality = 0
        self.southCellQuality = 0
        self.eastCellQuality = 0
        self.westCellQuality = 0
        self.northCellVisited = ""
        self.southCellVisited = ""
        self.eastCellVisited = ""
        self.westCellVisited = ""
        self.job = 1 # the job attribute will determine if the bee is a worker(0) or a scout(1)

    def findNonVisited(self, moveOptions):
        length = len(moveOptions)
        position =  random.randint(0,length-1)
        for item in moveOptions:
            if item[2] == "F":
                return item[0]
        return moveOptions[position][0] 
    def move(self, territory):
        """
        Move the drone inside the territory based on certain conditions and rules.

        Args:
            territory (list): A 2D list representing the territory where the drone is moving. Each element in the list is a Cell object.

        Returns:
            None
        """
        moveOptions = self.getMoveOptions(territory)
        sortedOptions = sorted(moveOptions, key=lambda x: x[1], reverse=True)
        options_number = len(sortedOptions)
        if options_number == 1:
            moveDirection = sortedOptions[0][0]
        if self.job == 0:
            moveDirection = self.findNonVisited(sortedOptions)
            self.job = 1
            self.changeCell(moveDirection)
            return
        else:
            if options_number == 2 and sortedOptions[0][1] == sortedOptions[1][1]:
                position = random.randint(0, 1)
                moveDirection = sortedOptions[position][0]
            elif options_number == 3:
                if sortedOptions[0][1] == sortedOptions[1][1]:
                    if sortedOptions[0][1] == sortedOptions[2][1]:
                        position = random.randint(0, 2)
                        moveDirection = sortedOptions[position][0]
                    else:
                        position = random.randint(0, 1)
                        moveDirection = sortedOptions[position][0]
                else:
                    moveDirection = sortedOptions[0][0]
            else:
                moveDirection = sortedOptions[0][0]
            self.job = 0
            self.changeCell(moveDirection)
            return

    def getMoveOptions(self, territory):
        """
        Determines the possible move options for the drone based on its current direction and the state of its neighboring cells.

        Args:
            territory (list): A 2D list representing the territory where the drone is moving. Each element in the list is a Cell object.

        Returns:
            list: A list of tuples representing the possible move options for the drone. Each tuple contains the direction and the cell quality of the corresponding move option.
        """
        self.checkNeighborState(territory)
        moveOptions = []

        if self.direction == "north":
            if self.eastValue == 0:
                moveOptions.append(("east", self.eastCellQuality, self.eastCellVisited))
            if self.westValue == 0:
                moveOptions.append(("west", self.westCellQuality, self.westCellVisited))
            if self.northValue == 0:
                moveOptions.append(("north", self.northCellQuality, self.northCellVisited))
            else:
                if len(moveOptions) == 0:
                    self.direction = "south"
                    moveOptions.append(("south", self.southCellQuality, self.southCellVisited))
                else:
                    self.changeDirection("north")

        elif self.direction == "south":
            if self.eastValue == 0:
                moveOptions.append(("east", self.eastCellQuality, self.eastCellVisited))
            if self.westValue == 0:
                moveOptions.append(("west", self.westCellQuality, self.westCellVisited))
            if self.southValue == 0:
                moveOptions.append(("south", self.southCellQuality, self.southCellVisited))
            else:
                if len(moveOptions) == 0:
                    self.direction = "north"
                    moveOptions.append(("north", self.northCellQuality, self.northCellVisited))
                else:
                    self.changeDirection("south")

        elif self.direction == "east":
            if self.northValue == 0:
                moveOptions.append(("north", self.northCellQuality, self.northCellVisited))
            if self.southValue == 0:
                moveOptions.append(("south", self.southCellQuality, self.southCellVisited))
            if self.eastValue == 0:
                moveOptions.append(("east", self.eastCellQuality, self.eastCellVisited))
            else:
                if len(moveOptions) == 0:
                    self.direction = "west"
                    moveOptions.append(("west", self.westCellQuality, self.westCellVisited))
                else:
                    self.changeDirection("east")

        elif self.direction == "west":
            if self.northValue == 0:
                moveOptions.append(("north", self.northCellQuality, self.northCellVisited))
            if self.southValue == 0:
                moveOptions.append(("south", self.southCellQuality, self.southCellVisited))
            if self.westValue == 0:
                moveOptions.append(("west", self.westCellQuality, self.westCellVisited))
            else:
                if len(moveOptions) == 0:
                    self.direction = "east"
                    moveOptions.append(("east", self.eastCellQuality, self.eastCellVisited))
                else:
                    self.changeDirection("west")

        return moveOptions

    def changeDirection(self, direction):
        """
        Randomly selects a new direction for the drone to move in, excluding the current direction.

        Args:
            direction (string): The current direction of the drone.

        Returns:
            string: The randomly selected new direction for the drone to move in.
        """
        cardinalPoints = ["north", "south", "east", "west"]
        cardinalPoints.remove(direction)
        newDirection = random.choice(cardinalPoints)
        self.direction = newDirection
        return newDirection

    def changeCell(self, moveDirection):
        """
        Update the position of the drone based on the given move direction.

        Args:
            moveDirection (str): The direction in which the drone should move. It can be one of the following values: "north", "south", "east", or "west".

        Returns:
            None: The method does not return any value. It only updates the position of the drone.
        """
        if moveDirection == "north":
            self.positionY -= 1
        elif moveDirection == "south":
            self.positionY += 1
        elif moveDirection == "east":
            self.positionX += 1
        elif moveDirection == "west":
            self.positionX -= 1

    def checkNeighborState(self, territory):
        """
        Check the state of neighboring cells in a territory grid.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            None. The methods update the values of northValue, southValue, eastValue, westValue, northCellQuality, southCellQuality, eastCellQuality, and westCellQuality attributes of the Drone instance.
        """
        self.checkNorthNeighbor(territory)
        self.checkSouthNeighbor(territory)
        self.checkEastNeighbor(territory)
        self.checkWestNeighbor(territory)

    def checkNorthNeighbor(self, territory):
        """
        Check the state of the neighbor cell in the north direction.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            None. The method updates the values of northValue and northCellQuality attributes of the Drone instance.
        """
        if self.positionY == 0:
            self.northValue = 1
        else:
            cell = territory[self.positionY-1][self.positionX]
            self.northValue = cell.value
            self.northCellQuality = cell.cellQuality
            self.northCellVisited = cell.visited

    def checkSouthNeighbor(self, territory):
        """
        Check the state of the neighbor cell in the south direction.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            None. The method updates the values of southValue and southCellQuality attributes of the Drone instance.
        """
        if self.positionY == len(territory) - 1:
            self.southValue = 1
        else:
            cell = territory[self.positionY+1][self.positionX]
            self.southValue = cell.value
            self.southCellQuality = cell.cellQuality

    def checkEastNeighbor(self, territory):
        """
        Check the state of the neighbor cell in the east direction.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            None. The method updates the values of eastValue and eastCellQuality attributes of the Drone instance.
        """
        if self.positionX == len(territory)-1:
            self.eastValue = 1
        else:
            cell = territory[self.positionY][self.positionX+1]
            self.eastValue = cell.value
            self.eastCellQuality = cell.cellQuality

    def checkWestNeighbor(self, territory):
        """
        Check the state of the neighbor cell in the west direction.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            None. The method updates the values of westValue and westCellQuality attributes of the Drone instance.
        """
        if self.positionX == 0:
            self.westValue = 1
        else:
            cell = territory[self.positionY][self.positionX-1]
            self.westValue = cell.value
            self.westCellQuality = cell.cellQuality

    def markVisitedCell(self, territory):
        """
        marks the cell as visited in the territory grid.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            territory: The updated territory grid with the cell marked as visited.
        """
        territory[self.positionY][self.positionX].visited = "V"
        return territory

    def reduceCellQuality(self, territory):
        """
        marks the cell as visited in the territory grid.

        Args:
            self: The instance of the Drone class.
            territory: A 2D grid representing the territory with cells.

        Returns:
            territory: The updated territory grid with the cell marked as visited.
        """
        cell = territory[self.positionY][self.positionX]
        if (cell.cellQuality > 0):
            cell.cellQuality = cell.cellQuality - 5
        else:
            cell.cellQuality = 0
        return territory


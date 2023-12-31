import random

# #This class will model both ants and bees
# #used on the ACO and BCO algorithms
class Drone:
    def __init__(self, initialDirection, initialX, initialY):
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
                moveOptions.append(("east", self.eastCellQuality))
            if self.westValue == 0:
                moveOptions.append(("west", self.westCellQuality))
            if self.northValue == 0:
                moveOptions.append(("north", self.northCellQuality))
            else:
                if len(moveOptions) == 0:
                    self.direction = "south"
                    moveOptions.append(("south", self.southCellQuality))
                else:
                    self.changeDirection("north")

        elif self.direction == "south":
            if self.eastValue == 0:
                moveOptions.append(("east", self.eastCellQuality))
            if self.westValue == 0:
                moveOptions.append(("west", self.westCellQuality))
            if self.southValue == 0:
                moveOptions.append(("south", self.southCellQuality))
            else:
                if len(moveOptions) == 0:
                    self.direction = "north"
                    moveOptions.append(("north", self.southCellQuality))
                else:
                    self.changeDirection("south")

        elif self.direction == "east":
            if self.northValue == 0:
                moveOptions.append(("north", self.northCellQuality))
            if self.southValue == 0:
                moveOptions.append(("south", self.southCellQuality))
            if self.eastValue == 0:
                moveOptions.append(("east", self.eastCellQuality))
            else:
                if len(moveOptions) == 0:
                    self.direction = "west"
                    moveOptions.append(("west", self.southCellQuality))
                else:
                    self.changeDirection("east")

        elif self.direction == "west":
            if self.northValue == 0:
                moveOptions.append(("north", self.northCellQuality))
            if self.southValue == 0:
                moveOptions.append(("south", self.southCellQuality))
            if self.westValue == 0:
                moveOptions.append(("west", self.westCellQuality))
            else:
                if len(moveOptions) == 0:
                    self.direction = "east"
                    moveOptions.append(("east", self.southCellQuality))
                else:
                    self.changeDirection("west")

        return moveOptions

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

 
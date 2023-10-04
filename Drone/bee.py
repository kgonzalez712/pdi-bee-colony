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
        self.job = 1 # the job attribute will determine if the bee is a worker(0) or a scout(1)
    
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
        moveDirection = sortedOptions[position][0]
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
            cell.cellQuality = random.randint(500, 1000)
        else:
            cell.cellQuality = 0
        return territory




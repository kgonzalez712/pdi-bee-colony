import random

class Cell:
    def __init__(self, value: int, swarmAlgorithm: int):
        """
        Initializes the attributes of a cell object.
    
        Args:
            value (int): The value of the cell. 0 -> free path | 1 -> wall 
            swarmAlgorithm (int): The swarm algorithm used to calculate the cell quality. 0 -> ACO | 1-> ABCO
        """
        self.value = value
        self.visited = "F" if self.value == 0 else "-" # F means not visited, V means visted and - is used for walls
    
        if swarmAlgorithm == 0:
            self.cellQuality = 0
        elif self.value != 1:
            self.cellQuality = random.randint(500, 1000)
        else:
            self.cellQuality = 0

        
    def reduceQuality(self):
        """
        Reduces the quality of the cell by 1 and returns the updated quality.

        Returns:
             The updated quality of the cell.
        """
        if(self.cellQuality > 0):
            self.cellQuality -= 0.0001
        else:
            self.cellQuality = random.randint(500, 1000)
        return self.cellQuality

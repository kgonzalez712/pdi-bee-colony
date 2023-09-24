class Cell:
    def __init__(self, value: int):
        self.value = value
        self.cellQuality = 0
        self.visited = "F" if self.value == 0 else "-"

    def reduceQuality(self):
        """
        Reduces the quality of the cell by 1 and returns the updated quality.

        Returns:
             The updated quality of the cell.
        """
        self.cellQuality -= 1
        return self.cellQuality

class Cell:

  def __init__(self, value):
    # If value = 0 is an empty space, if it is not 0 then is an obstacle
    self.value = value
    self.cellQuality = 0
    if self.value == 0:
      self.visited = "F"
    else:
      self.visited = "-"
  
  def reduceQuality(self):
    self.cellQuality = self.cellQuality - 1
    return self.cellQuality

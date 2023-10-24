import random
import numpy as np


def createMaze(size, mapType):
  """Creates a square maze of size x size.

  Args:
    size: The size of the maze.

  Returns:
    A square maze of size x size.
  """

  matrix = np.zeros((size+2, size+2), dtype=int)
  matrix[0, 6:] = 1
  matrix[-1, :] = 1
  matrix[2:, 0] = 1
  matrix[:, -1] = 1
  matrix[-1, :] = 1
  innerMatrix = matrix[2:-2, 2:-2]
  if mapType == 2:
    result = populate(innerMatrix,size)
  else:
    result = randomMaze(len(innerMatrix),innerMatrix)
  matrix[2:2+(len(innerMatrix)), 2:2+(len(innerMatrix))] = result
  write_maze_to_txt_file(matrix, "maze.txt")
  return matrix


def createBlock():
  option = random.randint(0,1)
  room = np.zeros((25, 25), dtype=int)
  if option == 1:
    return createRoom(room)
  else:
    return createWall(room)
  
def createRoom(room):
  option = random.randint(0,2)
  if option == 0:
    room[0, :] = 1
    room[-1, :] = 1
    room[:, 0] = 1
    room[:, -1] = 1
    room[-1, :] = 1
    roomType = random.randint(0,4)
    if roomType == 0:
      return Room1(room)
    elif roomType == 1:
      return Room2(room)
    elif roomType == 2:
      return Room3(room)
    else:
      return Room4(room)
  else:
    wall = random.randint(6,20)
    room[0, 6:] = 1
    room[0:wall, 0] = 1
    room[:wall, -1] = 1
    room[wall, :] = 1
    return room

def Room1(room):
  for i in range(12, 17):
    room[i, 0] = 0
  for j in range(0,5):
    room[12,j] = 1
  return room

def Room2(room):
  for i in range(12, 17):
    room[i, 24] = 0
  for j in range(20,24):
    room[11,j] = 1
  return room

def Room3(room):
  for i in range(11, 17):
    room[0, i] = 0
  for j in range(0, 5):
    room[j, 11] = 1 
  return room

def Room4(room):
  for i in range(12, 17):
    room[24, i] = 0
  for j in range(21, 24):
    room[j, 17] = 1
  return room

def createWall(room):
  option = random.randint(0,3)
  if option == 0:
    return Wall1(room)
  elif option == 1:
    return Wall2(room)
  else:
    return Wall3(room)

def Wall1(room):
  for i in range(10, 16):
    room[10, i] = 1
  for j in range(10, 16):
    room[j, 10] = 1
  return room

def Wall2(room):
  for i in range(10, 16):
    room[10, i] = 1
  for j in range(4, 10):
    room[j, 10] = 1
  return room

def Wall3(room):
  for j in range(7,15):
    for i in range(7, 15):
      room[j, i] = 1
  return room

def randomMaze(size,inner):
  # Add obstacles randomly.
  for i in range(size):
    for j in range(size):
      if random.random() < 0.3:
        inner[i][j] = 1

  return inner
# Write the maze to a txt file.
def write_maze_to_txt_file(maze, filename):
  with open(filename, "w") as f:
    for row in maze:
      f.write("".join([str(cell) for cell in row]) + "\n")

def populate(inner,size):
  # Specify the step size for inserting the 5x5 matrix
  step = 40
  # Iterate over rows of the 50x50 matrix with a step of 'step'
  for insert_row in range(0, size, step):
      # Iterate over columns of the 50x50 matrix with a step of 'step'
      for insert_col in range(0, size, step):
          room = createBlock()
          # Insert the 5x5 matrix into the 50x50 matrix at the current position
          inner[insert_row:insert_row + 25, insert_col:insert_col + 25] = room
  return inner



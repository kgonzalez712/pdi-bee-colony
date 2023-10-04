import random
import numpy as np


def create_maze(size):
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
  matrix[-1, :] = 1 # Added this line to fix the bottom border

  return matrix



def create_room():
  room = np.zeros((25, 25), dtype=int)
  room[0, :] = 1
  room[-1, :] = 1
  room[:, 0] = 1
  room[:, -1] = 1
  room[-1, :] = 1 # Added this line to fix the bottom border
  return Wall1(room)

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

def Wall1(room):
  room[0, :] = 0
  room[-1, :] = 0
  room[:, 0] = 0
  room[:, -1] = 0
  room[-1, :] = 0 
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

# Write the maze to a txt file.
def write_maze_to_txt_file(maze, filename):
  with open(filename, "w") as f:
    for row in maze:
      f.write(" ".join([str(cell) for cell in row]) + "\n")

def populate(inner,room):
  # Specify the step size for inserting the 5x5 matrix
  resul = inner
  step = 50

  # Iterate over rows of the 50x50 matrix with a step of 'step'
  for insert_row in range(0, 300, step):
      # Iterate over columns of the 50x50 matrix with a step of 'step'
      for insert_col in range(0, 300, step):
          # Insert the 5x5 matrix into the 50x50 matrix at the current position
          resul[insert_row:insert_row + 25, insert_col:insert_col + 25] = room
  return resul

maze = create_maze(300)
inner_matrix = maze[1:-1, 1:-1]
room = create_room()
res = populate(inner_matrix,room)
mazeF = maze[1:1 + 300, 1:1 + 300] = res

# Write the maze to a txt file.
write_maze_to_txt_file(maze, "maze.txt")
# Write the maze to a txt file.
write_maze_to_txt_file(room, "room.txt")
# Write the maze to a txt file.
write_maze_to_txt_file(inner_matrix, "inner.txt")
# Write the maze to a txt file.
write_maze_to_txt_file(res, "res.txt")
write_maze_to_txt_file(mazeF, "mazeF.txt")



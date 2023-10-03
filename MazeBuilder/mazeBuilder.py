import random
import numpy as np


def create_maze(size):
  """Creates a square maze of size x size.

  Args:
    size: The size of the maze.

  Returns:
    A square maze of size x size.
  """

  matrix = np.zeros((size, size), dtype=int)
  matrix[0, :] = 1
  matrix[-1, :] = 1
  matrix[:, 0] = 1
  matrix[:, -1] = 1
  matrix[-1, :] = 1 # Added this line to fix the bottom border
  inner_matrix = matrix[1:-1, 1:-1]

  return matrix

# maze = create_maze(25)

# Write the maze to a txt file.
def write_maze_to_txt_file(maze, filename):
  with open(filename, "w") as f:
    for row in maze:
      f.write(" ".join([str(cell) for cell in row]) + "\n")

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

room = create_room()

  

# Write the maze to a txt file.
write_maze_to_txt_file(room, "maze.txt")

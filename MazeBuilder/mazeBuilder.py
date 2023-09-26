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

maze = create_maze(50)

# Write the maze to a txt file.
def write_maze_to_txt_file(maze, filename):
  with open(filename, "w") as f:
    for row in maze:
      f.write(" ".join([str(cell) for cell in row]) + "\n")

# Write the maze to a txt file.
write_maze_to_txt_file(maze, "maze.txt")

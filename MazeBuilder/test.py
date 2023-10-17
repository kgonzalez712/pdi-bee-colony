import random

def randomMaze(size):
  maze = [[0 for i in range(size)] for j in range(size)]

  # Add obstacles randomly.
  for i in range(size):
    for j in range(size):
      if random.random() < 0.3:
        maze[i][j] = 1

  return maze

# Write the maze to a txt file.
def write_maze_to_txt_file(maze, filename):
  with open(filename, "w") as f:
    for row in maze:
      f.write(" ".join([str(cell) for cell in row]) + "\n")

maze = randomMaze(20)
write_maze_to_txt_file(maze,"testMaze.txt")


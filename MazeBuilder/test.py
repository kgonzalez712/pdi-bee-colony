import numpy as np

# Create a 50x50 matrix filled with zeros
matrix_50x50 = np.zeros((50, 50), dtype=int)

# Create a 5x5 matrix filled with ones
matrix_5x5 = np.ones((5, 5), dtype=int)

# Specify the step size for inserting the 5x5 matrix
step = 10

# Iterate over rows of the 50x50 matrix with a step of 'step'
for insert_row in range(0, 50, step):
    # Iterate over columns of the 50x50 matrix with a step of 'step'
    for insert_col in range(0, 50, step):
        # Insert the 5x5 matrix into the 50x50 matrix at the current position
        matrix_50x50[insert_row:insert_row + 5, insert_col:insert_col + 5] = matrix_5x5

# Print the resulting 50x50 matrix
for row in matrix_50x50:
    print(" ".join(map(str, row)))

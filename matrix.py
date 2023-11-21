def input_matrix(rows, cols):
    matrix = []
    print(f"Enter elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j] += matrix[i][j]
    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

# Get user input for the number of matrices, rows, and columns
num_matrices = int(input("Enter the number of matrices: "))
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

# Input matrices from the user
matrices = []
for _ in range(num_matrices):
    matrix = input_matrix(rows, cols)
    matrices.append(matrix)

# Add matrices
result_matrix = add_matrices(matrices)

# Display the result
print("\nSum of the matrices:")
display_matrix(result_matrix)

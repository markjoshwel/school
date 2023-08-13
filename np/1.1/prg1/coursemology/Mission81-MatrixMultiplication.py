def matrix_multiplication(A, B):
    rows_A = len(A)
    rows_B = len(B)

    cols_A = len(A[0])
    cols_B = len(B[0])

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    if cols_A != rows_B:
        return []

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C
    C = []

    return C


# Define matrix A as a nested list and matrix B as a list
# remove these statements when submitting in Coursemology
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [1, 2, 3]

# Do not remove the next line that calls the function
C = matrix_multiplication(A, B)

# Display the result
print(C)

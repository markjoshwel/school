A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

B = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]


def matrixmult(A, B):
    # valid matrix guard clause
    if not (len(A[0]) == len(B)):
        return None

    B_bycol = [[] for _ in B[0]]
    for row in B:
        for ind, col in enumerate(row):
            B_bycol[ind].append(col)

    C = []
    for A_row in A:
        C_row = []
        for B_col in B_bycol:
            total = 0
            for row, col in zip(A_row, B_col):
                total += row * col
            C_row.append(total)
        C.append(C_row)

    return C


# C = matrixmult(A, B)
# print(C)

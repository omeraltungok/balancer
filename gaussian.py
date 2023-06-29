"""Swap two rows in a matrix"""
def swap_rows(A, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]

"""Divide a row"""
def divide_row(A, row, divisor):
    for i in range(len(A[row])):
        A[row][i] = A[row][i] / divisor

"""Subtract one row from another row multiplied by a number"""
def row_eliminate(A, row_to_change, row_changer, ratio):
    for i in range(len(A[row_to_change])):
        A[row_to_change][i] -= ratio * A[row_changer][i]
"""Find the row with the maximum value in the given column"""
def findMaxRow(A, row, col):
    max_row = row
    for r in range(row + 1, len(A)):
        if abs(A[r][col]) > abs(A[max_row][col]):
            max_row = r
    return max_row

"""Does Gaussian elimination"""
def gauss_eliminate_algorithm(A):

    row_count = len(A) # num X num
    col_count = len(A[0])

    row = 0
    for col in range(col_count - 1): # -1 because the last column is for constants
        # Find the row with the maximum value in the current column
        max_row = findMaxRow(A, row, col)
        # Swap the current row with the row that has the maximum value
        swap_rows(A, row, max_row)
        # If after the swap the leading coefficient in the current row is 0, skip to the next column
        if A[row][col] == 0:
            continue
        # Divide the current row by its first element according to colomn
        divide_row(A, row, A[row][col])
        # For each row under the current row, subtract an the row so that the entry in the current column is 0
        for r in range(row + 1, row_count):
            row_eliminate(A, r, row, A[r][col])
        # Move to the next row and column
        row += 1

    # do row-reduction from the last row up to the first row
    for r in range(row_count - 1, -1, -1):
        for r2 in range(r-1, -1, -1):
            row_eliminate(A, r2, r, A[r2][r])
    return A
def is_saddle_point(matrix,row,col):
    points_in_row=matrix[row]
    points_in_col=[matrix_row[col] for matrix_row in matrix]
    saddle_point=matrix[row][col]==min(points_in_col) and matrix[row][col]==max(points_in_row)
    return saddle_point
def saddle_points(matrix):
    if len(set(map(len,matrix)))>1:
        raise ValueError("irregular matrix")
    points=[]
    for row_idx, row in enumerate(matrix):
        for col_idx, point in enumerate(row):
            if is_saddle_point(matrix, row_idx, col_idx):
                points.append({'row':row_idx + 1,'column':col_idx + 1})
    return points
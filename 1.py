# Напишите функцию для транспонирования матрицы .


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def transpone():
    trans_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[i][j] = matrix[j][i]
    return trans_matrix
print(matrix)
# transpone()
print(transpone())
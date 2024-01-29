#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[el**2 for el in row] for row in matrix]



    sqared_matrix = []
    for row in matrix:
        sqare_list = []
        for element in row:
            square_list.append(element**2)
            squared_matrix.append(square_list)
        return squared_matrix

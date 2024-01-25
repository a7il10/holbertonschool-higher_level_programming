#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for list_ in row:
            if list_ != row[-1]:
                print("{:d}".format(list_), end=" ")
            else:
                print("{:d}".format(list_), end="")
        print()

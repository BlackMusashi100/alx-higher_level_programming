#!/usr/bin/python3
square_matrix_simple = _import_('0-square_matrix_simple').square_matrix_simple

matrix = [[0,1,2],[3,4,5],[6,7,8]]

matrix = [x**2 for x in range(3)]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

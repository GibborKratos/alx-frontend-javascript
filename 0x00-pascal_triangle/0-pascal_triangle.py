#!/usr/bin/python3
""
Returns a list of lists of integers representing the Pascal’s triangle of n
""


def pascal_triangle(n):
    
    if n <= 0:
        # Return an empty list if n is not positive
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start a new row with the first element 1
        row = [1]
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            # from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with the last element 1
        row.append(1)
        triangle.append(row)

    return (triangle)

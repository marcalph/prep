def zero_striping(matrix: list[list[int]]) -> None:
    rows, cols = set(), set()
    m, n = len(matrix), len(matrix[0])
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                rows.add(i)
                cols.add(j)
    for col in cols:
        for i in range(m):
            matrix[i][col] = 0
    for row in rows:
        for j in range(n):
            matrix[row][j] = 0

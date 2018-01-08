def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb in bombs:
        (row_i, col_i) = bomb
        field[row_i][col_i] = -1
        for i in range(row_i - 1, row_i + 2):
            for j in range(col_i - 1, col_i + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols
                    and field[i][j] != -1):
                    field[i][j] += 1
    return field


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + '\n '.join(list_rows) + ']'


print mine_sweeper([[0, 2], [2, 0], [3, 3]], 3, 3)

def chessboard(N:int):
    for i in range(N):
        matrix_line = ''
        if i%2==0:
            matrix_line='* '*(int(N/2))
        else:
            matrix_line=' *'*(int(N/2))
        print(matrix_line)
    print('\n')
def frame(N:int):
    for i in range(N):
        matrix_line = ''
        if i == 0 or i == N-1:
            matrix_line= '*'*N
        else:
            matrix_line = '*'+' '*(N-2)+'*'
        print(matrix_line)
    print('\n')
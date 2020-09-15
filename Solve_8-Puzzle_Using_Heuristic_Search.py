import os


def heuristic_value(matrix, goal_matrix):
    H = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != goal_matrix[i][j]:
                H += 1
    return H


def swap(board, i, j, x, y):
    newBoard = [row[:] for row in board]
    newBoard[i][j] = board[x][y]
    newBoard[x][y] = '0'
    return newBoard


def print_matrix(initial_matrix, goal_matrix):
    print(" ~ : Initial Matrix :~  ->  ~ : Goal Matrix : ~")
    print("\t\t---------\t\t\t\t---------")
    for i in range(3):
        print("\t\t|", initial_matrix[i][0], initial_matrix[i][1], initial_matrix[i][2], "|", end="\t\t")
        print("\t\t|", goal_matrix[i][0], goal_matrix[i][1], goal_matrix[i][2], "|", end="\n")
    print("\t\t---------\t\t\t\t---------")
    print()


def add_into_queue(queue, new_matrix, prev, path, heuristic):
    if new_matrix not in prev:
        previse = prev + [new_matrix]
        queue.append((previse, path, heuristic))


def is_convert(a, b):
    x = []
    y = []
    for i in a:
        for j in i:
            x.append(j)
    for i in b:
        for j in i:
            y.append(j)
    for i in x:
        if i not in y:
            return False
    return True


def a_star(init_matrix, goal_matrix):
    if init_matrix == goal_matrix:
        print(" ~: Initial Matrix is equal to Goal Matrix :~ ")
        return
    if not is_convert(init_matrix, goal_matrix):
        print(" ~: Goal Matrix can't be Archived :~ ")
        return
    prev = [init_matrix]
    Result = None
    queue = [(prev, [], heuristic_value(prev[-1], goal_matrix))]
    while queue:
        queue.sort(key=lambda k: k[2])
        prev, path, _ = queue.pop(0)
        matrix = prev[-1]
        i = None
        j = None
        for x in range(3):
            for y in range(3):
                if matrix[x][y] == '0':
                    i = x
                    j = y
                    break
        NewMatrix = None
        NewHeuristic = 5000
        NewPath = None
        if i > 0:
            Matrix1 = swap(matrix, i, j, i - 1, j)
            if Matrix1 == goal_matrix:
                Result = path + ["U"]
                break
            Heuristic = heuristic_value(Matrix1,goal_matrix)
            if NewHeuristic > Heuristic:
                NewMatrix = Matrix1
                NewHeuristic = Heuristic
                NewPath = path + ["U"]
        if i < 2:
            Matrix2 = swap(matrix, i, j, i + 1, j)
            if Matrix2 == goal_matrix:
                Result = path + ["D"]
                break
            Heuristic = heuristic_value(Matrix2,goal_matrix)
            if NewHeuristic > Heuristic:
                NewMatrix = Matrix2
                NewHeuristic = Heuristic
                NewPath = path + ["D"]
        if j > 0:
            Matrix3 = swap(matrix, i, j, i, j - 1)
            if Matrix3 == goal_matrix:
                Result = path + ["L"]
                break
            Heuristic = heuristic_value(Matrix3,goal_matrix)
            if NewHeuristic > Heuristic:
                NewMatrix = Matrix3
                NewHeuristic = Heuristic
                NewPath = path + ["L"]
        if j < 2:
            Matrix4 = swap(matrix, i, j, i, j + 1)
            if Matrix4 == goal_matrix:
                Result = path + ["R"]
                break
            Heuristic = heuristic_value(Matrix4,goal_matrix)
            if NewHeuristic > Heuristic:
                NewMatrix = Matrix4
                NewHeuristic = Heuristic
                NewPath = path + ["R"]
        if NewMatrix is not None:
            add_into_queue(queue, NewMatrix, prev, NewPath, NewHeuristic)
    if Result is not None:
        print("\n ~: Path Found :~ \n")
        print(" -> ".join(Result))
    else:
        print("\n ~: Path Not Found :~ ")


def read_matrix():
    Matrix = []
    for i in range(3):
        M = []
        for j in range(3):
            M.append(input("Enter a Value of"+str(i)+", "+str(j)+": "))
        Matrix.append(M)
    return Matrix


if __name__ == '__main__':
    Goal_Matrix = [['1', '2', '3'],
                   ['4', '5', '6'],
                   ['7', '8', '0']]
    Init_Matrix = [['0', '5', '2'],
                   ['1', '4', '3'],
                   ['7', '8', '6']]
    while True:
        os.system("cls")
        print()
        print("==================================================")
        print("||     ~ : Created By  : Yogesh Kumar : ~       ||")
        print("||     ~ : Roll Number : 205118090    : ~       ||")
        print("||==============================================||")
        print("|| 1. For Change Given Matrix                   ||")
        print("|| 2. For Change Goal Matrix                    ||")
        print("|| 3. For Find Goal Using A Star Algorithm      ||")
        print("|| 4. For Print Both Matrix                     ||")
        print("|| 5. For Exit                                  ||")
        print("||==============================================||")
        operation = input(" Select a Operation : ")
        if operation == '1':
            Init_Matrix = read_matrix()
        elif operation == '2':
            Goal_Matrix = read_matrix()
        elif operation == '3':
            a_star(Init_Matrix, Goal_Matrix)
        elif operation == '4':
            print_matrix(Init_Matrix, Goal_Matrix)
        elif operation == '5':
            exit()
        else:
            print("\n Please Select a correct operation")
        input("\n Press Enter to Continue ...")

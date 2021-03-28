puzzle = [

        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
]


def solve(pu):

    find = find_empty(pu)
    if not find:
        return True
    else:
        row, col  = find

    for i in range(1,10):
        if correct(pu,i , (row,col)):
            pu[row][col] = i

            if solve(pu):
                return True

            pu[row][col] = 0

    return False

def correct(pu, num, pos):
    # Check row
    for i in range(len(pu[0])):
        if pu[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(len(pu)):
        if pu[i][pos[1]] == num and pos[0] != i:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if pu[i][j] == num and (i,j) != pos:
                return  False

    return True




def print_puzzle(pu):

    for i in range(len(pu)):
        if i % 3== 0 and i != 0:
            print("_________________________")

        for j in range(len(pu[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8 :
                print(pu[i][j])

            else:
                print(str(pu[i][j]) + " ", end="")

print_puzzle(puzzle)

def find_empty(pu):
    for i in range(len(pu)):
        for j in range(len(pu[0])):
            if pu[i][j] == 0:
                return (i, j)   #row,col

    return None


solve(puzzle)
print("=========================")
print_puzzle(puzzle)

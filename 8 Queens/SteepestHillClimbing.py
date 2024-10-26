import time
import random

FAILED = False

# heuristic cost
def getCollisionNum(board):
    num = 0
    for col in range(len(board)):
        for anotherCol in range(col+1, len(board)):
            if board[col] == board[anotherCol]:
                num += 1 # collied in the same row
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                num += 1 # collied diagonally
    return num

def step_steepestHillClimbing(board):
    collisionNumBoard = {}
    smallestColisionNum = getCollisionNum(board)
    for col in range(len(board)):
        for row in range(len(board)):
            if board[col] == row:
                continue
            originRow = board[col]
            board[col] = row
            collisionNumBoard[(row,col)] = getCollisionNum(board)
            board[col] = originRow
            
    for point,value in collisionNumBoard.items():
        if value < smallestColisionNum:
            smallestColisionNum = value
    
    smallestCollisionPoint = []
    for point,value in collisionNumBoard.items():
        if value == smallestColisionNum:
            smallestCollisionPoint.append(point)
    
    if len(smallestCollisionPoint) == 0:
        global FAILED
        FAILED = True
        return board
    
    random.shuffle(smallestCollisionPoint)
    board[smallestCollisionPoint[0][1]] = smallestCollisionPoint[0][0]
    return board


def solution_steepestHillClimbing(board):
    maxRound = 200
    count = 0
    while True:
        collisionNum = getCollisionNum(board)
        if collisionNum == 0:
            return board
        board = step_steepestHillClimbing(board)
        count += 1
        if count > maxRound:
            global FAILED
            FAILED = True
            return board
        
        
def main():
    title = "EightQueens_steepestRandomHillClimbing"
    startTime = time.perf_counter()
    successCase = 0
    totalCase = 0
    result = title + " result:\n\n"
    with open("8 Queens/eightQueensTest.txt", "r") as ins:
        for line in ins:
            print("case: ", totalCase)
            global FAILED
            FAILED = False
            totalCase += 1
            board = []
            for col in line.split():
                board.append(int(col))
            board = solution_steepestHillClimbing(board)
            if FAILED:
                result += "Failed!"
            else:
                successCase += 1
                for col in range(len(board)):
                    result += str(board[col]) + " "
            result += "\n"
    
    endTime = time.perf_counter()
    result += "\nTotal time: " + str(endTime - startTime) + '\n'
    result += "Total case number: " + str(totalCase) + ", Success case number: " + str(successCase) + '\n'
    result += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    print(result)
    
    f = open("8 Queens/" + title + '.txt', 'w')
    f.write(result)
    f.close()
    
if __name__ == '__main__':
    main()
    


    
import random

def createNumber(minNum,maxNum,exist):
    while True:
        number = random.randint(minNum,maxNum)
        if number in exist:
            continue
        else:
            exist.append(number)
            return number

def checkLine(hole,size):
    reach = bingo = 0
    for row in range(size):
        count = sum(hole[row][col] for col in range(size))
        if count == size:
            bingo += 1
        elif count == size - 1:
            reach += 1

    for col in range(size):
        count = sum(hole[row][col] for row in range(size))
        if count == size:
            bingo += 1
        elif count == size - 1:
            reach += 1

    count = sum(hole[i][i] for i in range(size))
    if count == size:
        bingo += 1
    elif count == size - 1:
        reach += 1

    count = sum(hole[i][size-1-i] for i in range(size))
    if count == size:
        bingo += 1
    elif count == size - 1:
        reach += 1
    return reach, bingo

def printCard(card, hole):
    for rowCard, rowHole in zip(card, hole):
        rowDisplay = []
        for num, mark in zip(rowCard, rowHole):
            if num == "FREE":
                rowDisplay.append("FREE")
            elif mark and num != "FREE":
                rowDisplay.append(f"({num:02d})")
            elif num != "FREE": 
                rowDisplay.append(f" {num:02d} ")
        print(' '.join(rowDisplay))

def createCard(size, existNumber):
    card = [[0] * size for _ in range(size)]
    hole = [[0] * size for _ in range(size)]
    mid = size // 2
    for i in range(size):
        for j in range(size):
            minNum = 1 + 15 * j
            maxNum = 15 * (j + 1)
            number = createNumber(minNum,maxNum,existNumber)
            card[i][j] = number
    card[mid][mid] = "FREE"
    hole[mid][mid] = True
    return card, hole

def markCard(card, hole, ball):
    for i in range(len(card)):
        for j in range(len(card[0])):
            if card[i][j] == ball:
                hole[i][j] = True
def main():
    existNumber = []
    existBall = []
    size = 5
    ballCount = 0
    card, hole = createCard(size, existNumber)
    while True:
        ballCount += 1
        ball = createNumber(1,75,existBall)
        print(f'Ball[{ballCount}]: {ball}')
        markCard(card, hole, ball)
        printCard(card, hole)
        reach, bingo = checkLine(hole,size)
        print(f'\nREACH: {reach}')
        print(f'BINGO: {bingo}')
        print("--------------------")
        if all(all(row) for row in hole):
            break
if __name__ == "__main__":
    main()
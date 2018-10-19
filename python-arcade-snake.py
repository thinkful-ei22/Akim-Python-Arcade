import pygame
import random
pygame.init()

screenWidth = 900
screenHeight = 900

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake")
# it's bad practice to draw in the main loop, so we'll take an object oriented--
# --approach for snake.

# the clock will be used to control the frame rate
clock = pygame.time.Clock()


class _Node:
    def __init__(self, x, y, next):
        self.width = 20
        self.height = 20
        self.xPos = x
        self.yPos = y
        self.next = next
        self.prevPos = {'xPos': x, 'yPos': y}

# implementing a linkedList variant for the snake.


class SnakeList:
    def __init__(self):
        self.head = None

    def insertFirst(self, xVal, yVal):
        self.head = _Node(xVal, yVal, self.head)

    def moveSnakeNodes(self):
        currentNode = self.head
        while currentNode != None:
            if currentNode.next != None:
                currentNode.next.xPos = currentNode.prevPos['xPos']
                currentNode.next.yPos = currentNode.prevPos['yPos']
            currentNode.prevPos['xPos'] = currentNode.xPos
            currentNode.prevPos['yPos'] = currentNode.yPos
            currentNode = currentNode.next

    def insertLast(self):
        if(self.head != None):
            tempNode = self.head
            while (tempNode.next != None):
                tempNode = tempNode.next

            tempNode.next = _Node(tempNode.xPos, tempNode.yPos, None)
            return
        else:
            self.insertFirst(xVal, yVal)


def redrawGameWindow(player, food):
    win.fill((0, 0, 0))
    currentNode = player.head
    counter = 1
    while (currentNode != None):
        if currentNode == player.head:
            pygame.draw.rect(win, (255, 0, 0), (currentNode.xPos,
                                                currentNode.yPos, currentNode.width, currentNode.height))
            currentNode = currentNode.next
        else:
            pygame.draw.rect(win, (255, 0, 255), (currentNode.xPos,
                                                  currentNode.yPos, currentNode.width, currentNode.height))
            currentNode = currentNode.next

    while counter <= 5:
        if food[counter] != None:
            pygame.draw.rect(
                win, (0, 255, 0), (food[counter]['xPos'], food[counter]['yPos'], 20, 20))
        counter += 1

    player.moveSnakeNodes()

    pygame.display.update()


def getRandomNumber():
    for x in range(1):
        return (5 + (30 * random.randint(-1, 28)))


def generateFood(obj, xVal, yVal):
    counter = 1
    while counter <= 5:
        if obj[counter] == None:
            obj[counter] = {}
            obj[counter]['xPos'] = xVal
            obj[counter]['yPos'] = yVal
            return obj
        counter += 1
    print('current food is full')
    print(obj)


def addFood(obj):
    randomX = getRandomNumber()
    randomY = getRandomNumber()
    generateFood(obj, randomX, randomY)


def deleteFood(player, food):
    foodLooper = 1
    while foodLooper <= 5:
        if food[foodLooper] != None:
            if player.head.xPos == food[foodLooper]['xPos'] and player.head.yPos == food[foodLooper]['yPos']:
                food[foodLooper] = None
                player.insertLast()
                print(food)
                return
        foodLooper += 1


def playerLose(obj):
    playerX = obj.head.xPos
    playerY = obj.head.yPos
    currentNode = obj.head.next
    if not 4 < playerX < 876:
        return True
    elif not 4 < playerY < 876:
        return True
    else:
        while currentNode != None:
            if currentNode != obj.head.next:
                if obj.head.xPos == currentNode.xPos and obj.head.yPos == currentNode.yPos:
                    return True
            currentNode = currentNode.next
    return False


# =========================MAIN LOOP=============================================
# make a custom event using pygame's USEREVENT
MAKEFOOD = pygame.USEREVENT+1

Snake = SnakeList()
currentFood = {1: None, 2: None, 3: None, 4: None, 5: None}
Snake.insertFirst(5, 5)
run = True
left = False
right = False
up = False
down = False
velocity = 30
pygame.time.set_timer(MAKEFOOD, 2500)
while run:

            # in case player quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # keyboard event handler
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT and right != True):
                left = True
                right = False
                up = False
                down = False
            if(event.key == pygame.K_RIGHT and left != True):
                left = False
                right = True
                up = False
                down = False
            if(event.key == pygame.K_UP and down != True):
                left = False
                right = False
                up = True
                down = False
            if(event.key == pygame.K_DOWN and up != True):
                left = False
                right = False
                up = False
                down = True

        if event.type == MAKEFOOD:
            addFood(currentFood)

    if(left == True):
        Snake.head.xPos -= velocity
    if(right == True):
        Snake.head.xPos += velocity
    if(up == True):
        Snake.head.yPos -= velocity
    if(down == True):
        Snake.head.yPos += velocity

    deleteFood(Snake, currentFood)

    lose = playerLose(Snake)
    if lose != False:
        left = False
        right = False
        up = False
        down = False
        Snake = SnakeList()
        Snake.insertFirst(5, 5)
        currentFood = {1: None, 2: None, 3: None, 4: None, 5: None}

    redrawGameWindow(Snake, currentFood)

    clock.tick(5)
pygame.quit()

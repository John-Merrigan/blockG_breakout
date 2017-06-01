# breakout.py
#
# No thank you, I don't need your help Woz.
#
# Name: J

from graphics import *
from random import *
from music import *
import math

# height and width of game's window in pixels
HEIGHT = 600
WIDTH = 800

# number of rows and columns of bricks
ROWS = 10
COLS = 20

# radius of ball in pixels
RADIUS = 10

# size of paddle in pixels
PADWIDTH = 60
PADHT = 10

# number of lives
LIVES = 3

# brick size
BRKWDTH = (WIDTH-COLS)/COLS - 4
BRKHT = 10

# bricks list (array)
bricks = []

# instantiate window
win = GraphWin("Breakout", WIDTH, HEIGHT)


def main():

    label0 = Text(Point(400, 180), "BREAKOUT")
    label0.setStyle("bold")
    label0.setSize(100)
    label0.setTextColor("BLACK")
    label0.draw(win)

    label1 = Text(Point(400, 300), "  Breakout_fireball: press 1")
    label1.setSize(36)
    label1.setTextColor("Dark Gray")
    label1.draw(win)

    label2 = Text(Point(400, 380), "Breakout_black: press 2")
    label2.setSize(36)
    label2.setTextColor("Dark Gray")
    label2.draw(win)

    label3 = Text(Point(400, 460), " Breakout_Kyle: press 3  ")
    label3.setSize(36)
    label3.setTextColor("Dark Gray")
    label3.draw(win)

    select = win.getKey()
    label1.undraw()
    label2.undraw()
    label3.undraw()
    label0.undraw()

    while select != "1" and select != "2" and select != "3":
        select = win.getKey()
    if select == "1":
        fireball()
    elif select == "2":
        black()
    elif select == "3":
        kyle()

#-------------------------------------------------------------------------------
#fireball

def fireball():
    # instantiate bricks
    initBricks()

    center=(200,300)
    # instantiate ball, centered in middle of window
    ball = initBall()


    # instantiate paddle, centered at bottom of window
    paddle = initPaddle()

    # instantiate scoreboard, centered in middle of window
    label = initScoreboard()

    # number of lives initially
    lives = LIVES

    # instantiate lives scorekeeper
    livesText = initLives()

    # number of points initially
    score = 0

    # number of bricks initially
    numBricks = COLS * ROWS

    # initial velocity
    xvelocity = 2.0
    yvelocity = 2.0
    angle = math.atan2(yvelocity, xvelocity)



    while True:

            # move ball move using xvelocity, yvelocity
            ball.move(xvelocity, yvelocity)

            # get x and y coordinate of center of ball (xBall, yBall)
            xBall= ball.getCenter().getX()
            yBall= ball.getCenter().getY()

            # bounce off edge of window
            if checkSides(xBall):
                xvelocity = -xvelocity
            if yBall <= 5:
                yvelocity = -yvelocity


            # if ball goes below paddle, decrease lives by 1
            if yBall + RADIUS >= 600:
                ball.undraw()
                lives = lives - 1
                updateLives(livesText,lives)
            # if no more lives, game over, else sleep 2 seconds and
                if lives == 0:
                    gameOver(label)
                else:
            # instantiate new ball
                    time.sleep(2)
                    ball = initBall()
                    xvelocity = 0
                    yvelocity = 2
                    ball.move(xvelocity, yvelocity)

            # paddle movement
            paddleMove(paddle)

            # if paddle hits ball reverse ball direction
            if padHit(paddle, xBall, yBall):
                angle = math.radians(270-((ball.getCenter().getX() - paddle.getCenter().getX()) * 2))
                xvelocity = - math.cos(angle) * 5
                yvelocity = math.sin(angle) * 5

            # detect collision with bricks
            for brick in bricks:
                # if ball collides with a brick, undraw the brick
                if checkCollision(brick, yBall, xBall):
                    brick.undraw()
                # remove the brick from the list (bricks.remove(brick))
                    bricks.remove(brick)
                # reverse the yvelocity
                    #yvelocity = -yvelocity
                # decrease the number of bricks by 1
                    numBricks = numBricks - 1
                # increase the score by 1
                    score = score + 1
                # update the scoreboard
                    updateScoreboard(label, score)
                # if no more brickes left you win!
                    if numBricks == 0:
                        youWin(label)


def initBricks():
    color= ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "RED", "ORANGE", "YELLOW", "GREEN", "BLUE"]

    for i in range (ROWS):
        for j in range (COLS):
            x = j * (BRKWDTH + 5) + 2
            y = i * (BRKHT + 5) + 2
            rect = Rectangle(Point(x, y), Point(x + BRKWDTH, y + BRKHT))
            rect.setFill(color[i])
            rect.draw(win)
            bricks.append(rect)



# instantiate paddle as a rectangle object, in bottom middle of window
def initPaddle():
    paddle= Rectangle(Point( 150, 560), Point(240, 590))
    paddle.setFill("BLACK")
    paddle.draw(win)
    return paddle

# instantiate ball as a circle in center of window below the scoreboard
def initBall():
    ball = Circle(Point(200,250), 6)
    ball.setFill("RED")
    ball.draw(win)
    return ball

# if ball touches left or right side of window, return True, else return False
def checkSides(xBall):
    if xBall + RADIUS >= 800 or xBall - RADIUS <= 0:
        return True
    else:
        return False

def paddleMove(paddle):
    user_event = win.checkKey()
    padPt = paddle.getP1()
    padX = padPt.getX()
    if user_event == "Left" and padX > 0:
        paddle.move(-20, 0)
    elif user_event == "Right" and padX + PADWIDTH < WIDTH:
        paddle.move(20, 0)

def padHit(paddle, xBall, yBall):
    pointPaddle = paddle.getCenter()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def initLives():
    anchorpoint = Point(60, HEIGHT - 20)
    livesText = Text(anchorpoint, "Lives Remaining: " + str(LIVES))
    livesText.draw(win)
    return livesText

def updateLives(livesText, lives):
    livesText.setText("Lives Remaining: " + str(lives))
    return livesText

def initScoreboard():
    x = WIDTH / 2
    y = HEIGHT / 2
    anchorPoint = Point(x, y)
    label = Text(anchorPoint, "0")
    label.setSize(36)
    label.setTextColor("Dark Gray")
    label.draw(win)
    return label

def checkCollision(brick, yBall, xBall):
    brickCorner = brick.getP2()
    xBrick = brickCorner.getX()
    yBrick = brickCorner.getY()
    if yBall > (yBrick - BRKHT-5) and yBall < yBrick+5  and xBall > (xBrick - BRKWDTH) and xBall < xBrick :
        return True
    else:
        return False

def padHit(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH + 30) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def updateScoreboard(label, score):
    label.setText(score)
    return label

def gameOver(label):
    updateScoreboard(label, "You Lose!")
    time.sleep(4)
    exit(0)

def youWin(label):
    updateScoreboard(label, "You Win!")
    time.sleep(4)
    exit(0)

#-------------------------------------------------------------------------------
#black

def black():

    win.setBackground("BLACK")

    #play a random song
    playMusic()


    # instantiate bricks
    initBricksM()



    center=(200,300)
    # instantiate ball, centered in middle of window
    ball = initBallM()


    # instantiate paddle, centered at bottom of window
    paddle = initPaddleM()

    # instantiate scoreboard, centered in middle of window
    label = initScoreboardM()

    # number of lives initially
    lives = LIVES

    # instantiate lives scorekeeper
    livesText = initLivesM()

    # number of points initially
    score = 0

    # number of bricks initially
    numBricks = COLS * ROWS

    # initial velocity
    xvelocity = (random() * 3 + 5)
    yvelocity = 2.5

    #wait for mouse click
    win.getMouse()

    while True:

            # move ball move using xvelocity, yvelocity
            ball.move(xvelocity, yvelocity)

            # get x and y coordinate of center of ball (xBall, yBall)
            xBall= ball.getCenter().getX()
            yBall= ball.getCenter().getY()

            # bounce off edge of window
            if checkSidesM(xBall):
                xvelocity = -xvelocity
            elif yBall == 0:
                yvelocity = -yvelocity -1


            # if ball goes below paddle, decrease lives by 1
            if yBall + RADIUS == 600:
                ball.undraw()
                lives = lives -1
                updateLivesM(livesText,lives)
                time.sleep(2)
            # if no more lives, game over, else sleep 2 seconds and
                if lives == 0:
                    gameOverM(label)
                else:
            # instantiate new ball
                    ball = initBallM()
                    ball.move(xvelocity, yvelocity)

            # paddle movement
            paddleMoveM(paddle)

            # if paddle hits ball reverse ball direction
            if padHitM(paddle, xBall, yBall):
                yvelocity = -yvelocity
                xvelocity = xvelocity

            # detect collision with bricks
            for brick in bricks:
                # if ball collides with a brick, undraw the brick
                if checkCollisionM(brick, yBall, xBall):
                    brick.undraw()
                # remove the brick from the list (bricks.remove(brick))
                    bricks.remove(brick)
                # reverse the yvelocity
                    yvelocity = -yvelocity
                # decrease the number of bricks by 1
                    numBricks = numBricks - 1
                # increase the score by 1
                    score = score + 1
                # update the scoreboard
                    updateScoreboardM(label, score)
                # if no more brickes left you win!
                    if numBricks == 0:
                        youWinM(label)


def initBricksM():
    color= ["WHITE", "BlACK", "WHITE", "BLACK", "WHITE", "BLACK", "WHITE", "BLACK", "WHITE", "BLACK"]

    for i in range (ROWS):
        for j in range (COLS):
            x = j * (BRKWDTH + 5) + 2
            y = i * (BRKHT + 5) + 2
            rect = Rectangle(Point(x, y), Point(x + BRKWDTH, y + BRKHT))
            rect.setFill(color[i])
            rect.draw(win)
            bricks.append(rect)



# instantiate paddle as a rectangle object, in bottom middle of window
def initPaddleM():
    paddle= Rectangle(Point( 150, 560), Point(240, 590))
    paddle.setFill("WHITE")
    paddle.draw(win)
    return paddle

# instantiate ball as a circle in center of window below the scoreboard
def initBallM():
    ball = Circle(Point(200,250), 10)
    ball.setFill("WHITE")
    ball.draw(win)
    return ball

# if ball touches left or right side of window, return True, else return False
def checkSidesM(xBall):
    if xBall + RADIUS >= 800 or xBall - RADIUS <= 0:
        return True
    else:
        return False

def paddleMoveM(paddle):
    user_event = win.checkKey()
    padPt = paddle.getP1()
    padX = padPt.getX()
    if user_event == "Left" and padX > 0:
        paddle.move(-35, 0)
    elif user_event == "Right" and padX + PADWIDTH < WIDTH:
        paddle.move(35, 0)

def padHitM(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def initLivesM():
    anchorpoint = Point(60, HEIGHT - 20)
    livesText = Text(anchorpoint, "Lives Remaining: " + str(LIVES))
    livesText.draw(win)
    return livesText

def updateLivesM(livesText, lives):
    livesText.setText("Lives Remaining: " + str(lives))
    return livesText

def initScoreboardM():
    x = WIDTH / 2
    y = HEIGHT / 2
    anchorPoint = Point(x, y)
    label = Text(anchorPoint, "0")
    label.setSize(36)
    label.setTextColor("Dark Gray")
    label.draw(win)
    return label

def checkCollisionM(brick, yBall, xBall):
    brickCorner = brick.getP2()
    xBrick = brickCorner.getX()
    yBrick = brickCorner.getY()
    if yBall - yBrick < 5 and xBall > (xBrick - BRKWDTH) and xBall < xBrick :
        return True
    else:
        return False

def padHitM(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def updateScoreboardM(label, score):
    label.setText(score)
    return label

def gameOverM(label):
    updateScoreboard(label, "You Lose!")
    time.sleep(4)
    exit(0)

def youWinM(label):
    updateScoreboard(label, "You Win!")
    time.sleep(4)
    exit(0)

#-------------------------------------------------------------------------------
#code

def kyle():
    win.setBackground("BLACK")
    # instantiate bricks
    initBricksK()



    center=(200,300)
    # instantiate ball, centered in middle of window
    ball = initBallK()


    # instantiate paddle, centered at bottom of window
    paddle = initPaddleK()

    # instantiate scoreboard, centered in middle of window
    label = initScoreboardK()

    # number of lives initially
    lives = LIVES

    # instantiate lives scorekeeper
    livesText = initLivesK()

    # number of points initially
    score = 0

    # number of bricks initially
    numBricks = COLS * ROWS

    # initial velocity
    xvelocity = (random() * 3 + 3)
    yvelocity = 2.5

    #wait for mouse click
    win.getMouse()

    while True:

        # move ball move using xvelocity, yvelocity
        ball.move(xvelocity, yvelocity)

        # get x and y coordinate of center of ball (xBall, yBall)
        xBall= ball.getCenter().getX()
        yBall= ball.getCenter().getY()

        # bounce off edge of window
        if checkSidesK(xBall):
            xvelocity = -xvelocity
        elif yBall == 0:
            yvelocity = -yvelocity


        # if ball goes below paddle, decrease lives by 1
        if yBall >= 600:
            ball.undraw()
            lives = lives - 1
            updateLivesK(livesText,lives)
            time.sleep(1)
        # if no more lives, game over, else sleep 2 seconds and
            if lives == 0:
                gameOverK(label)
            else:
        # instantiate new ball
                ball = initBallK()
                ball.move(xvelocity, yvelocity)

        # paddle movement
        paddleMoveK(paddle)

        # if paddle hits ball reverse ball direction
        if padHitK(paddle, xBall, yBall):
            yvelocity = -yvelocity

        # detect collision with bricks
        for brick in bricks:
            # if ball collides with a brick, undraw the brick
            if checkCollisionK(brick, yBall, xBall):
                brick.undraw()
            # remove the brick from the list (bricks.remove(brick))
                bricks.remove(brick)
            # reverse the yvelocity
                yvelocity = -yvelocity + .1
            # decrease the number of bricks by 1
                numBricks = numBricks - 1
            # increase the score by 1
                score = score + 1
            # update the scoreboard
                updateScoreboardK(label, score)
            # if no more brickes left you win!
                if numBricks == 0:
                    youWinK(label)

def initBricksK():
    color= ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE","RED", "ORANGE", "YELLOW", "GREEN", "BLUE"]

    for i in range (ROWS):
        for j in range (COLS):
            x = j * (BRKWDTH + 5) + 2
            y = i * (BRKHT + 5) + 2
            rect = Rectangle(Point(x, y), Point(x + BRKWDTH, y + BRKHT))
            rect.setFill(color[i])
            rect.draw(win)
            bricks.append(rect)



# instantiate paddle as a rectangle object, in bottom middle of window
def initPaddleK():
    paddle= Rectangle(Point( 150, 560), Point(240, 590))
    paddle.setFill("WHITE")
    paddle.draw(win)
    return paddle

# instantiate ball as a circle in center of window below the scoreboard
def initBallK():
    ball = Circle(Point(200,250), 10)
    ball.setFill("BLUE")
    ball.draw(win)
    return ball

# if ball touches left or right side of window, return True, else return False
def checkSidesK(xBall):
    if xBall + RADIUS >= 800 or xBall - RADIUS <= 0:
        return True
    else:
        return False

def paddleMoveK(paddle):
    user_event = win.checkKey()
    padPt = paddle.getP1()
    padX = padPt.getX()
    if user_event == "Left" and padX > 0:
        paddle.move(-50, 0)
    elif user_event == "Right" and padX + PADWIDTH < WIDTH:
        paddle.move(50, 0)

def padHitK(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def initLivesK():
    anchorpoint = Point(60, HEIGHT - 20)
    livesText = Text(anchorpoint, "Lives Remaining: " + str(LIVES))
    livesText.draw(win)
    return livesText

def updateLivesK(livesText, lives):
    livesText.setText("Lives Remaining: " + str(lives))
    return livesText

def initScoreboardK():
    x = WIDTH / 2
    y = HEIGHT / 2
    anchorPoint = Point(x, y)
    label = Text(anchorPoint, "0")
    label.setSize(36)
    label.setTextColor("Dark Gray")
    label.draw(win)
    return label

def checkCollisionK(brick, yBall, xBall):
    brickCorner = brick.getP2()
    xBrick = brickCorner.getX()
    yBrick = brickCorner.getY()
    if yBall - yBrick < 5 and xBall > (xBrick - BRKWDTH) and xBall < xBrick :
        return True
    else:
        return False

def padHitK(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
        return True
    else:
        return False

def updateScoreboardK(label, score):
    label.setText(score)
    return label

def gameOverK(label):
    updateScoreboard(label, "You Lose!")
    time.sleep(4)
    exit(0)

def youWinK(label):
    updateScoreboard(label, "You Win!")
    time.sleep(4)
    exit(0)




if __name__ == "__main__":
    main()

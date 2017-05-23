# breakout.py
#
# CS50 AP
# Name: J

from graphics import *
from random import *

# height and width of game's window in pixels
HEIGHT = 600
WIDTH = 400

# number of rows and columns of bricks
ROWS = 5
COLS = 10

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
    xvelocity = (random() * 3 + 2)
    yvelocity = 2.0

    #wait for mouse click
    win.getMouse()

    while True:

            # move ball move using xvelocity, yvelocity
            ball.move(xvelocity, yvelocity)

            # get x and y coordinate of center of ball (xBall, yBall)
            xBall= ball.getCenter().getX()
            yBall= ball.getCenter().getY()

            # bounce off edge of window
            if checkSides(xBall):
                xvelocity = -xvelocity
            elif yBall == 0:
                yvelocity = -yvelocity


            # if ball goes below paddle, decrease lives by 1
            if yBall + RADIUS == 600:
                ball.undraw()
                lives = lives - 1
                updateLives(livesText,lives)
            # if no more lives, game over, else sleep 2 seconds and
                if lives == 0:
                    gameOver(label)
                else:
            # instantiate new ball
                    ball = initBall()
                    ball.move(xvelocity, yvelocity)

            # paddle movement
            paddleMove(paddle)

            # if paddle hits ball reverse ball direction
            if padHit(paddle, xBall, yBall):
                yvelocity = -yvelocity

            # detect collision with bricks
            for brick in bricks:
                # if ball collides with a brick, undraw the brick
                if checkCollision(brick, yBall, xBall):
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
                    updateScoreboard(label, score)
                # if no more brickes left you win!
                    if numBricks == 0:
                        youWin(label)


def initBricks():
    color= ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE"]

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
    ball = Circle(Point(200,250), 10)
    ball.setFill("BLUE")
    ball.draw(win)
    return ball

# if ball touches left or right side of window, return True, else return False
def checkSides(xBall):
    if xBall + RADIUS >= 400 or xBall - RADIUS <= 0:
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
    pointPaddle = paddle.getP1()
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
    if yBall - yBrick < 5 and xBall > (xBrick - BRKWDTH) and xBall < xBrick :
        return True
    else:
        return False

def padHit(paddle, xBall, yBall):
    pointPaddle = paddle.getP1()
    xPaddle = pointPaddle.getX()
    yPaddle = pointPaddle.getY()
    if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
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

if __name__ == "__main__":
    main()

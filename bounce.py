from graphics import *
import vlc

# instantiate window
win = GraphWin("window", 600, 600)

# instantiate a point with (x, y) coordinates of (160, 120)
center = Point(160, 120)

# instantiate ball with center at (160, 120)
ball = Circle(center, 20)

# fill the circle with black
ball.setFill("BLACK")

# draw the circle to the window
ball.draw(win)

velocity = 2
p = vlc.MediaPlayer("file:///Users/admin/Desktop/Jimmy Cliff-Breakout.mp3")
p.play()

while True:


    # move ball along x-axis
    ball.move(velocity, 0)

    # get x-coordinate of circle
    centerBall = ball.getCenter()
    xBall = centerBall.getX()

    # bounce off right edge of window
    if xBall + 20 > 320:
        velocity = -velocity
    # bounce off left edge of window
    elif xBall - 20 < 0:
        velocity = -velocity


exit(0)

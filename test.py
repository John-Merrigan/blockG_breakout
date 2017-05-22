# play game
while True:

    # move ball move using xvelocity, yvelocity
    # TODO

    # get x and y coordinate of center of ball (xBall, yBall)
    # TODO

    # bounce off edge of window
    # TODO

    # if ball goes below paddle, decrease lives by 1
    # if no more lives, game over, else sleep 2 seconds and
    # TODO

    # instantiate new ball
    # TODO

    # paddle movement
    if key== "left":
        paddleMove(-10, 0)
    elif key=="right":
        paddleMove(10,0)

    # if paddle hits ball reverse ball direction
     #if 455> = x+radius >= 450 and p1Y <= y <= p2Y:
         #dx = -dx


    # detect collision with bricks
    for brick in bricks:
        # if ball collides with a brick, undraw the brick
        # remove the brick from the list (bricks.remove(brick))
        # reverse the yvelocity
        # decrease the number of bricks by 1
        # increase the score by 1
        # update the scoreboard
        # if no more brickes left you win!
        # TODO



# wait for click before exiting
win.getMouse()
win.close()

# all done!
exit(0)

def move_right():
    turn_left()
    turn_left()
    turn_left()
    move()

while not at_goal():
    if wall_on_right() == False:
        move_right()
    elif wall_in_front == False:
        move()
    elif wall_in_front() == True:
        turn_left()
        if wall_in_front() == False:
            move()
        else:
            turn_left()
    else:
        move()

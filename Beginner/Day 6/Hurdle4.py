def move_right():
    turn_left()
    turn_left()
    turn_left()
    move()

def move_down():
    while front_is_clear() == True:
            move()
    turn_left()
    
    
while not at_goal():
    if wall_in_front() == True:
        turn_left()
        while wall_on_right() == True:
            move()
        move_right()
        move_right()
        move_down()
    else:
        move()

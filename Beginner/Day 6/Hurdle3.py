def move_right():
    turn_left()
    turn_left()
    turn_left()
    move()

def jump():
    turn_left()
    move()
    move_right()
    move_right()
    turn_left()
    
while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        jump()

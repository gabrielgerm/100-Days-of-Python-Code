def move_right():
    turn_left()
    turn_left()
    turn_left()
    move()

def jump():
    move()
    turn_left()
    move()
    move_right()
    move_right()
    turn_left()
    
    
while at_goal() == False:
    jump()

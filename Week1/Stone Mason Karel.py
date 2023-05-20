from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    turn_left()
    build_column()
    continue_moving()  
    build_south()
    move_straight()
    build_column()
    continue_moving()
    build_column()
    turn_right()
    turn_left()
    turn_left()
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def build_column():
    if  no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
        if no_beepers_present():
            put_beeper()
            
            
def continue_moving():
    if front_is_blocked():
        turn_right()
    for i in range(4):
            move()
    turn_right()
    
def build_south():
    while facing_south():
        if no_beepers_present():
            put_beeper()
            move()
            if front_is_blocked():
                turn_left()
                
                
def move_straight():
    if no_beepers_present():
        put_beeper()
    for i in range(4):
        move()
    if not_facing_north():
        turn_left()
        

if __name__ == '__main__':
    main()
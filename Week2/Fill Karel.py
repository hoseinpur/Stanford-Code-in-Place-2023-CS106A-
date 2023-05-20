from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():

    filling()
    
def turn_around():
   turn_left()
   turn_left()
   
   
def filling():
    while no_beepers_present():
        while front_is_clear(): # put beeper and go till end
            put_beeper()
            move()
        put_beeper()    
        turn_around()           # turn around 
        while front_is_clear(): # return until clear
            move()
            
        turn_around()
        turn_left()             # turned toward up
        
        if front_is_clear():    # if front is clear, 
                                #turn toward right and repeat from the beginning
            move()
            turn_around()
            turn_left()
        
        else:
            turn_around()
            turn_left()
            while front_is_clear(): # return until clear
                move()
            pass    
    
   
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
from graphics import *
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    heightmiddle = CANVAS_HEIGHT // 2
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, heightmiddle, "red")
if __name__ == '__main__':
    main()
from graphics import Canvas
import time 
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 
intial_direction = 'ArrowLeft'
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    blue = canvas.create_rectangle(0,0,SIZE,SIZE,'Blue')
    x_red = random.randint(0,CANVAS_WIDTH)
    y_red = random.randint(0,CANVAS_HEIGHT)
    red = canvas.create_rectangle(x_red,y_red,x_red + SIZE,y_red + SIZE,'red')
    
    # TODO: your code here
    # intial value set to 0
    start_x = 0
    start_y = 0
    
    while True:
        move_right(canvas,blue, start_x,start_y)

        
def left_direction():
    start_x = -start_x

##def move_right(canvas,blue, start_x,start_y):
 #   intial_direction = 'ArrowRight'
 #   while True:
 #       start_x = start_x + SIZE
 #       canvas.moveto(blue,start_x,start_y)   
 #       time.sleep(DELAY) 
 #       if canvas.get_last_key_press() == 'ArrowDown':
 #           intial_direction = 'ArrowDown'
 #           move_down(canvas,blue, start_x,start_y)
            
def move_down(canvas,blue, start_x,start_y):
    while True:
        start_y = start_y + SIZE
        canvas.moveto(blue,start_x,start_y)   
        time.sleep(DELAY) 
        if canvas.get_last_key_press() == 'ArrowUp':
            intial_direction = 'ArrowUp'
            move_up(canvas,blue, start_x,start_y)

def move_left(canvas,blue, start_x,start_y):
        start_x = start_x - SIZE
        canvas.moveto(blue,start_x,start_y)   
        time.sleep(DELAY)

def move_up(canvas,blue, start_x,start_y):
    while True:
        start_y = start_y - SIZE
        canvas.moveto(blue,start_x,start_y)   
        time.sleep(DELAY)
if __name__ == '__main__':
    main()
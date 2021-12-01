from tkinter.constants import TRUE
import snakelib

width = 0  # initialized in play_snake
height = 0  # initialized in play_snake
ui = None  # initialized in play_snake
SPEED = 10
keep_running = True

def play_snake(init_ui):
    global width, height, ui, keep_running
    
    def determine_apple_position(l):
        def create_inital_list(h,w):
            a = [ [0]*w for i in range(h)]

            c = 0
            for i in range(h):
                for j in range(w):
                
                    a[i][j] = c
                    c += 1
            return a
        def get_the_number_of_possible_placement():
            for i in range(height):
                for j in range(width):
                    if [i,j] in l:
                        a[i][j] = "S"
            n = 0
            for i in range(height):
                for j in range(width):
                    if a[i][j] != "S":
                        a[i][j] = n
                        n +=1
            return n
        def give_correct_corrdinates(n):
            for i in range(height):
                for j in range(width):
                    if a[i][j] == n:
                        return j,i
        a = create_inital_list(height,width)
        nrFreeSpots = get_the_number_of_possible_placement()
        
        return give_correct_corrdinates(ui.random(nrFreeSpots))

       
        
    def draw(x,y):
        ui.place(x,y,ui.SNAKE)   
        if [y,x] in list_of_points_in_the_snake and [y,x] != list_of_points_in_the_snake[0]:
            ui.set_game_over()
        elif [y,x] == list_of_points_in_the_snake[0]:
            list_of_points_in_the_snake.append([y,x])
            list_of_points_in_the_snake.pop(0)
        else: 
            list_of_points_in_the_snake.append([y,x])
            ui.place(list_of_points_in_the_snake[0][1],list_of_points_in_the_snake[0][0],ui.EMPTY)
            list_of_points_in_the_snake.pop(0)
        ui.show()
        
    ui = init_ui
    width, height = ui.board_size()
    x = 1
    y = 0

    list_of_points_in_the_snake = []
    list_of_points_in_the_snake.append([0,0])
    list_of_points_in_the_snake.append([0,1])
    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake) 
  
    ui.place(0,0,ui.SNAKE)
    ui.place(1,0,ui.SNAKE)
    ui.place(apple_x,apple_y,ui.FOOD)
    ui.show()
    current_direction = "r"
    while keep_running:
        
        event = ui.get_event()
        left_border = 0
        upper_border = 0
        right_border = width-1
        down_border = height-1
        list_of_possible_moves = ["d","u","l","r"]

        if event.name == "alarm":
            

            if x < right_border and current_direction == "r":                
                x +=1
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
              
                    draw(x,y)
            elif x <= right_border and current_direction =="l" and x != 0:
                x -= 1
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
            elif current_direction == "d" and y != down_border:
                y +=1
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
            elif current_direction =="u" and y != upper_border:
                y -=1
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
            elif current_direction =="u" and y == upper_border:
                y = down_border
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
            elif current_direction =="d" and y == down_border:
                y = upper_border
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
            elif x == left_border:
                x = right_border
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
            elif x == right_border:
                x = left_border
                if x == apple_x and y == apple_y:
                    ui.place(x,y,ui.SNAKE) 
                    list_of_points_in_the_snake.append([y,x])
                    apple_x, apple_y = determine_apple_position(list_of_points_in_the_snake)
                    ui.place(apple_x,apple_y,ui.FOOD)
                    ui.show()  
                else: 
                    draw(x,y)
        if event.name == "quit":
            keep_running = False             
        elif event.data in list_of_possible_moves:
                current_direction = event.data
     


if __name__ == "__main__":
    # do this if running this module directly
    # (not when importing it for the tests)
    ui = snakelib.SnakeUserInterface(10, 10)
    ui.set_animation_speed(SPEED)
    play_snake(ui)

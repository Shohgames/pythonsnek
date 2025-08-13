#main code for the snake game
import random

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = {
    'w':UP,
    's':DOWN,
    'a':LEFT,
    'd':RIGHT
}

class Snake:
    def __init__(self, initbody, initdirection):
        self.body = initbody #initital body from the tuple
        self.direction = initdirection 
    def take_step(self, position):
        self.body = [position] + self.body[:-1] #when executed, it slices the end of the snake and puts it forward. 
    def set_direction(self, direction):
        self.direction = direction
    def head(self):
        #pass for debug
        return self.body[0]
        


class Apple:
    def __init__(self, position):
        self.position = position


class Game:
    def __init__(self, height, width, wall_mode=True):
        self.height = height
        self.width = width
        self.snake = Snake([(0,0),(1,0),(2,0),(3,0)], DOWN)
        self.wall_mode = wall_mode
        self.score = 0
        self.apple = self.spawn_apple()
    
    def spawn_apple(self):
        while True:
            pos = (random.randint(0, self.width-1),random.randint(0, self.height-1))
            if pos not in self.snake.body:
                return Apple(pos)

    def collision_self(self, position):
        return position in self.snake.body
    def board_matrix(self):
        #Matrix filled with "None"
        #Here it will return a 2d list of self.height and self.width with None elemnetns
        matrix = [[" " for _ in range(self.width)] for _ in range(self.height)]
        #Draw the snake
        for pos in self.snake.body[1:]:
            x, y = pos
            if 0 <= y < self.height and 0 <= x < self.width:
                    matrix[y][x] = "0"
        #snakehead draw func
        head_x, head_y = self.snake.head()
        if 0 <= head_y < self.height and 0 <= head_x < self.width:
            matrix[head_y][head_x] = "X"
        apple_x, apple_y = self.apple.position
        if 0 <= apple_x < self.height and 0 <= apple_y < self.width:
            matrix[apple_x][apple_y]="@"
        return matrix
    
    def render(self):
        matrix = self.board_matrix()
        #Prints the top border, it makes the first corner with + and then makes - times whatever and adds the final +
        print("+" + "-" * self.width + "+")
        #print each row with the same logic
        for row in matrix:
            #make sure to add "space_key" otherwise the board will have no inner space
            #make sure to print actual matix content and not space otherwise it will go over it
            #print("|" + " " * self.width + "|") < not this!
            print("|" + "".join(row) + "|")
        #print bottom border with the same logic
        print("+" + "-" * self.width + "+")
        print("score:",self.score)


    def move_snake(self):
        head_x, head_y = self.snake.head()
        dx, dy = self.snake.direction
        new_x = head_x + dx
        new_y = head_y + dy

        if self.wall_mode:
            if not (0 <= new_x < self.width and 0 <= new_y < self.height):
                print("Crashed into the wall! Game over!")
                print("Final score:", self.score)
                exit()
        else:
            new_x = new_x % self.width
            new_y = new_y % self.height
        
        new_position = (new_x, new_y)
        if self.collision_self(new_position):
            print("You crashed into yourself! Game over!")
            print("Final score:", self.score)
            exit()
        
        if new_position == self.apple.position:
            self.score += 1
            self.snake.body = [new_position] + self.snake.body 
            self.apple = self.spawn_apple()
        else:
            self.snake.take_step(new_position)
                #'''old code'''            
                    #wrap it ro the board
        
                    # new_x = max(0,min(self.width -1, new_x))
                    # new_y = max(0, min(self.height -1, new_y))
        self.snake.take_step((new_x, new_y))
        #height and width printer below for debug, no need to print it ingame
    
    def opposite_direction(self, dir1, dir2):
        return (dir1[0] == -dir2[0] and dir1[1] == -dir2[1])    
    
class Debug:
    def __init__(self, state, height=None, width=None):
        self.state = state
        self.height = height
        self.width = width
        if state == True:
            print("Height:", self.height)
            print("Width:", self.width)
        elif state == False:
            pass

def main():
    print("Choose your game mode!")
    print("(1) Die on the wall")
    print("(2) Warp on the wall")
    choice = input("Enter 1 or 2:")
    wall_mode = True if choice == "1" else False
    game = Game(10, 25, wall_mode)
    debug = Debug(False, game.height, game.width)
    while True: 
        game.render()
        move = input("Move (WASD + ENTER, Enter to continue), and press Q to quit!: ").lower()
        if move == 'q':
            print("Thanks for playing!")
            break
        if move in DIRECTIONS:
            new_dir = DIRECTIONS[move]
            #stop reversing
            if not game.opposite_direction(game.snake.direction, new_dir):
                game.snake.set_direction(new_dir)
        game.move_snake()

if __name__ == "__main__":
    main()





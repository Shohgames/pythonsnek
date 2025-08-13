#main code for the snake game

UP = (0,1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self, initbody, initdirection):
        self.body = initbody #initital body from the tuple
        self.direction = initdirection 
    def take_step(self, position):
        self.body = [position] + self.body[:-1] #when executed, it slices the end of the snake and puts it forward. 
    def set_direction(self, direction):
        self.direction = direction
    def head(self):
        #pass for now
        pass
        


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0,0),(1,0),(2,0),(3,0)], UP)

    
    def board_matrix(self):
        #Matrix filled with "None"
        #Here it will return a 2d list of self.height and self.width with None elemnetns
        matrix = [[None for _ in range(self.width)] for _ in range(self.height)]
        #Draw the snake
        for pos in self.snake.body[1:]:
            x, y = pos
            if 0 <= y < self.height and 0 <= x < self.width:
                    matrix[y][x] = "0"
        
    
    def render(self):
        matrix = self.board_matrix()
        #Prints the top border, it makes the first corner with + and then makes - times whatever and adds the final +
        print("+" + "-" * self.width + "+")
        #print each row with the same logic
        for row in matrix:
            #make sure to add "space_key" otherwise the board will have no inner space
            print("|" + " " * self.width + "|")
        #print bottom border with the same logic
        print("+" + "-" * self.width + "+")


        #height and width printer below for debug, no need to print it ingame
        #print("Height:", self.height)
        #print("Width:", self.width)

game = Game(10, 25)
game.render()



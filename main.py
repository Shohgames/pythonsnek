#main code for the snake game
class Snake:
    pass

class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def board_matrix(self):
        # Matrix filled with "None"
        # Here it will return a 2d list of self.height and self.width with None elemnetns
        return [[None for _ in range(self.width)] for _ in range(self.height)]
    
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

game = Game(10, 20)
game.render()



#main code for the snake game

# Fixed Snake Game - Terminal Based
import random

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = {
    'w': UP,
    's': DOWN,
    'a': LEFT,
    'd': RIGHT
}

class Snake:
    def __init__(self, initbody, initdirection):
        self.body = initbody  # initial body from the tuple
        self.direction = initdirection 
    
    def take_step(self, position):
        self.body = [position] + self.body[:-1]  # move head forward, remove tail
    
    def grow(self, position):
        self.body = [position] + self.body  # add head without removing tail
    
    def set_direction(self, direction):
        self.direction = direction
    
    def head(self):
        return self.body[0]

class Apple:
    def __init__(self, position):
        self.position = position

class Game:
    def __init__(self, height, width, wall_mode=True):
        self.height = height
        self.width = width
        # Start snake in a safe position within bounds
        start_x = width // 2
        start_y = height // 2
        self.snake = Snake([(start_x, start_y), (start_x, start_y + 1), (start_x, start_y + 2)], UP)
        self.wall_mode = wall_mode
        self.score = 0
        self.apple = self.spawn_apple()
    
    def spawn_apple(self):
        while True:
            pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if pos not in self.snake.body:
                return Apple(pos)

    def collision_self(self, position):
        return position in self.snake.body
    
    def board_matrix(self):
        # Create matrix filled with spaces
        matrix = [[" " for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw the snake body (excluding head)
        for pos in self.snake.body[1:]:
            x, y = pos
            if 0 <= y < self.height and 0 <= x < self.width:
                matrix[y][x] = "o"
        
        # Draw snake head
        head_x, head_y = self.snake.head()
        if 0 <= head_y < self.height and 0 <= head_x < self.width:
            matrix[head_y][head_x] = "X"
        
        # Draw apple (FIXED: correct coordinate bounds)
        apple_x, apple_y = self.apple.position
        if 0 <= apple_y < self.height and 0 <= apple_x < self.width:
            matrix[apple_y][apple_x] = "@"
        
        return matrix
    
    def render(self):
        matrix = self.board_matrix()
        print("\n" * 2)  # Clear some space
        
        # Print top border
        print("+" + "-" * self.width + "+")
        
        # Print each row
        for row in matrix:
            print("|" + "".join(row) + "|")
        
        # Print bottom border
        print("+" + "-" * self.width + "+")
        print(f"Score: {self.score}")

    def move_snake(self):
        head_x, head_y = self.snake.head()
        dx, dy = self.snake.direction
        new_x = head_x + dx
        new_y = head_y + dy

        # Handle wall collision or wrapping
        if self.wall_mode:
            if not (0 <= new_x < self.width and 0 <= new_y < self.height):
                print("Crashed into the wall! Game over!")
                print(f"Final score: {self.score}")
                return False  # Game over
        else:
            new_x = new_x % self.width
            new_y = new_y % self.height
        
        new_position = (new_x, new_y)
        
        # Check self collision
        if self.collision_self(new_position):
            print("You crashed into yourself! Game over!")
            print(f"Final score: {self.score}")
            return False  # Game over
        
        # Check if apple is eaten
        if new_position == self.apple.position:
            self.score += 1
            self.snake.grow(new_position)  # Grow snake
            self.apple = self.spawn_apple()  # Spawn new apple
        else:
            self.snake.take_step(new_position)  # Normal move
        
        return True  # Game continues
    
    def opposite_direction(self, dir1, dir2):
        return (dir1[0] == -dir2[0] and dir1[1] == -dir2[1])

class Debug:
    def __init__(self, state, height=None, width=None):
        self.state = state
        self.height = height
        self.width = width
        if state:
            print(f"Height: {self.height}")
            print(f"Width: {self.width}")

def main():
    print("Welcome to Terminal Snake!")
    print("Choose your game mode:")
    print("(1) Die on wall collision")
    print("(2) Wrap around walls")
    
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice! Please enter 1 or 2.")
    
    wall_mode = True if choice == "1" else False
    game = Game(15, 30, wall_mode)
    debug = Debug(False, game.height, game.width)
    
    print("\nControls:")
    print("W = Up, A = Left, S = Down, D = Right")
    print("Q = Quit")
    print("Press Enter after each move!")
    
    while True: 
        game.render()
        move = input("\nMove (WASD + Enter, or Q to quit): ").lower().strip()
        
        if move == 'q':
            print("Thanks for playing!")
            break
        
        if move in DIRECTIONS:
            new_dir = DIRECTIONS[move]
            # Prevent reversing into self
            if not game.opposite_direction(game.snake.direction, new_dir):
                game.snake.set_direction(new_dir)
            else:
                print("Can't reverse direction!")
                continue
        elif move == '':
            # Allow empty input to continue in current direction
            pass
        else:
            print("Invalid input! Use W/A/S/D or Q to quit.")
            continue
        
        # Move snake and check if game continues
        if not game.move_snake():
            break

if __name__ == "__main__":
    main()





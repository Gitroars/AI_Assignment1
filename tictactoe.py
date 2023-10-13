import math, copy

class TicTacToe():
    def __init__(self, state=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.state = state
        self.current_player = 1  # 'x' starts first

    def display_board(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        for row in self.state:
            print(f"{symbols[row[0]]}|{symbols[row[1]]}|{symbols[row[2]]}")
            print("-+-+-")

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.state[row][col] = self.current_player
            return True
        return False

    def is_valid_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.state[row][col] == 0:
            
            return True
        
        return False

    def switch_player(self):
        self.current_player = -self.current_player

    



    def expand_state(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    child = (i, j)
                    children.append(child)
        return children

    def minimax(self, depth, isMaxPlayer):
        if self.terminal_node()[0] or depth == 0:
            return self.terminal_node()

        if isMaxPlayer:
            v_max = -math.inf
            children = self.expand_state()
            for pos in children:
                child = copy.deepcopy(self.state)
                child[pos[0]][pos[1]] = 1
                v = self.minimax(depth - 1, not isMaxPlayer)
                v_max = max(v_max, v)
            return v_max
        else:
            v_min = math.inf
            children = self.expand_state()
            for pos in children:
                child = copy.deepcopy(self.state)
                child[pos[0]][pos[1]] = -1
                v = self.minimax(depth - 1, not isMaxPlayer)
                v_min = min(v_min, v)
            return v_min


    def terminal_node(self):
        result = 0
        isGameOver = True


        #Check for 0s
        isEmpty = None
        for row in range(3):
            for col in range(3):
                if self.state[row][col] != 0: 
                    isEmpty = True

        isGameOver = not isEmpty

        #Check rows
        for row in range(3):
            sum = 0
            for col in range(3):
                sum +=  self.state[row][col]
            if sum == 3: 
                isGameOver = True
                result = 10
            if sum == -3: 
                isGameOver = True
                result = -10

        # Check columns
        for col in range(3):
            if self.state[0][col] + self.state[1][col] + self.state[2][col] == 3:
                isGameOver = True
                result = 10
            elif self.state[0][col] + self.state[1][col] + self.state[2][col] == -3:
                isGameOver = True
                result = -10

        #check for diagonal win
        if (self.state[0][0] + self.state[1][1] + self.state[2][2] == 3) or (self.state[0][2] + self.state[1][1] + self.state[2][0] == 3):
            isGameOver = True
            result = 10
        elif (self.state[0][0] + self.state[1][1] + self.state[2][2] == -3) or (self.state[0][2] + self.state[1][1] + self.state[2][0] == -3):
            isGameOver = True
            result = -10

       

        return [isGameOver, result]



    
    def find_best_move(self):
        best_move = None
        best_eval = -math.inf

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    self.state[i][j] = 1
                    move_eval = self.minimax(0, False)
                    self.state[i][j] = 0

                    if move_eval[1] > best_eval:
                        best_eval = move_eval[1]
                        best_move = (i, j)

        return best_move


    
    
def play_game():
    game = TicTacToe()
    while True:
        if game.current_player == 1:
            print("AI is playing...")
            best_move = game.find_best_move()
            row, col = best_move
        else:
            print(f"Human is playing...")

        game.display_board()  # Display the board before the player's move

        if game.current_player == -1:
            while True:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if game.is_valid_move(row, col):
                    game.make_move(row, col)
                    break
        else:
            game.make_move(row, col)

        game_result = game.terminal_node()
        if game_result[0]:
            if game_result[1] == 10:
                print("AI wins!")
            elif game_result[1] == -10:
                print("Human wins!")
            else:
                print("It's a tie!")
            break

        game.display_board()  # Display the board after the player's move

        game.switch_player()

if __name__ == "__main__":
    play_game()








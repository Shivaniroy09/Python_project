import os

class TicTacToe:
    def __init__(self):
        self.board = ["-" for _ in range(9)]
        self.current_player = 1

    def display_board(self):
        print("\nCurrent Board:")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")

    def make_move(self, position):
        if self.board[position] == "-":
            self.board[position] = "X" if self.current_player == 1 else "O"
            return True
        return False

    def switch_player(self):
        self.current_player = 1 if self.current_player == 2 else 2

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "-":
                return self.board[combo[0]]
        return None

    def is_draw(self):
        return "-" not in self.board

    def save_game_state(self):
        with open("game_state.txt", "w") as file:
            file.write(",".join(self.board) + "\n")
            file.write(f"Player Turn: {self.current_player}\n")
        print("Game state saved!")

    def load_game_state(self):
        if os.path.exists("game_state.txt"):
            with open("game_state.txt", "r") as file:
                data = file.readlines()
                self.board = data[0].strip().split(",")
                self.current_player = int(data[1].strip().split(": ")[1])
            print("Game state loaded!")
        else:
            print("No saved game found. Starting a new game.")

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Player 1: X")
        print("Player 2: O")

        self.load_game_state()

        while True:
            self.display_board()
            print(f"Player {self.current_player}, enter your move (1-9) or 's' to save and quit:")
            move = input().strip()

            if move.lower() == 's':
                self.save_game_state()
                break

            if not move.isdigit() or not (1 <= int(move) <= 9):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            position = int(move) - 1

            if not self.make_move(position):
                print("Position already taken. Try again.")
                continue

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"Player {1 if winner == 'X' else 2} ({winner}) wins!")
                break

            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

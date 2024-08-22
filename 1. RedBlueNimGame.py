import argparse
import random

class RedBlueNimGame:
    def __init__(self, num_red, num_blue, version, first_player, depth):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.first_player = first_player
        self.depth = depth
        self.board = {"Red": num_red, "Blue": num_blue}
        self.score = 0

    def print_board(self):
        print(f"Remaining Marbles: Red: {self.board['Red']}, Blue: {self.board['Blue']}")

    def valid_move(self, prompt):
        while True:
            try:
                move = int(input(prompt))
                if move < 1 or move > 2:
                    raise ValueError
                if move > self.board["Red"] and move > self.board["Blue"]:
                    raise ValueError
                return move
            except ValueError:
                print("Invalid move. Please try again.")

    def remove_marbles(self, color, move):
        self.board[color] -= move

    def game_over(self):
        return self.board["Red"] == 0 or self.board["Blue"] == 0

    def calculate_score(self):
        self.score = self.board["Red"] * 2 + self.board["Blue"] * 3

    def evaluate_board(self):
        return self.board["Red"] - self.board["Blue"]

    def minimax(self, depth, alpha, beta, is_maximizing):
        if self.game_over():
            if self.version == "Standard":
                return -1 if self.board["Red"] == 0 else 1
            else:
                return 1 if self.board["Blue"] == 0 else -1
        if depth == 0:
            return self.evaluate_board()

        if is_maximizing:
            return self.maximize(depth, alpha, beta)
        else:
            return self.minimize(depth, alpha, beta)
    
    def maximize(self, depth, alpha, beta):
        best_score = -float("inf")
        moves = self.move_ordering()
        random.shuffle(moves)
        for color, num_marbles in moves:
            if self.board[color] >= num_marbles:
                self.remove_marbles(color, num_marbles)
                score = self.minimax(depth - 1, alpha, beta, False)
                self.board[color] += num_marbles
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    
    def minimize(self, depth, alpha, beta):
        best_score = float("inf")
        moves = self.move_ordering()
        random.shuffle(moves)
        for color, num_marbles in moves:
            if self.board[color] >= num_marbles:
                self.remove_marbles(color, num_marbles)
                score = self.minimax(depth - 1, alpha, beta, True)
                self.board[color] += num_marbles
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

    def move_ordering(self):
        if self.version == "Standard":
            return [("Red", 2), ("Blue", 2), ("Red", 1), ("Blue", 1)]
        else:
            return [("Blue", 1), ("Red", 1), ("Blue", 2), ("Red", 2)]

    def best_move(self):
        best_move = None
        best_score = float("-inf")
        moves = self.move_ordering()
        random.shuffle(moves)
        for color, move in moves:
            if self.board[color] >= move:
                self.remove_marbles(color, move)
                score = self.minimax(self.depth - 1, False, float("-inf"), float("inf"))
                self.board[color] += move
                if score > best_score:
                    best_score = score
                    best_move = (color, move)
        return best_move

    def play_game(self):
        current_player = self.first_player
        while not self.game_over():
            self.print_board()
            if current_player == "Human":
                self.human_turn()
            else:
                self.computer_turn()
            current_player = self.switch_player(current_player)
        self.end_game(current_player)

    def human_turn(self):
        color = input("Enter the color of marbles to remove (Red or Blue): ").capitalize()
        move = self.valid_move(f"Enter the number of marbles to remove from {color}: ")
        if move > self.board[color]:
            print("Invalid move. Please try again.")
            return
        self.remove_marbles(color, move)

    def computer_turn(self):
        color, move = self.best_move()
        if color:
            self.remove_marbles(color, move)
            print(f"Computer removed {move} {color} marbles.")

    def switch_player(self, current_player):
        return "Computer" if current_player == "Human" else "Human"

    def end_game(self, current_player):
        self.calculate_score()
        if self.version == "Standard":
            winner = "Human" if current_player == "Computer" else "Computer"
        else:
            winner = "Human" if current_player == "Human" else "Computer"
        print(f"Game Over! {winner} wins!")
        print(f"Score: {self.score}")

def main():
    parser = argparse.ArgumentParser(description="Red Blue Nim Game")
    parser.add_argument("num_red", type=int, help="Number of Red Marbles", nargs='?', default=10)
    parser.add_argument("num_blue", type=int, help="Number of Blue Marbles", nargs='?', default=10)
    parser.add_argument("--version", type=str, choices=["Standard", "Misere"], default="Standard", help="Game Type (Standard or Misere)")
    parser.add_argument("--first_player", type=str, choices=["Human", "Computer"], default="Computer", help="First Player (Human or Computer)")
    parser.add_argument("--depth", type=int, default=10, help="Depth of Minimax Algorithm")

    args = parser.parse_args()

    game = RedBlueNimGame(args.num_red, args.num_blue, args.version, args.first_player, args.depth)
    game.play_game()

if __name__ == "__main__":
    main()

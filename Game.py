import random
import sys

opponent_symbol = "X"
computer_symbol = "O"
vacant_symbol = "-"

row_1 = ["1", "2", "3"]
row_2 = ["4", "5", "6"]
row_3 = ["7", "8", "9"]

column_1 = ["1", "4", "7"]
column_2 = ["2", "5", "8"]
column_3 = ["3", "6", "9"]

diagonal_1 = ["1", "5", "9"]
diagonal_2 = ["3", "5", "7"]

rows = [row_1, row_2, row_3]
columns = [column_1, column_2, column_3]
diagonals = [diagonal_1, diagonal_2]

winning_combinations = [*rows, *columns, *diagonals]

tic_tac_toe_grid = {
    "1": vacant_symbol, "2": vacant_symbol, "3": vacant_symbol,
    "4": vacant_symbol, "5": vacant_symbol, "6": vacant_symbol,
    "7": vacant_symbol, "8": vacant_symbol, "9": vacant_symbol
}
available_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
played_moves = []
game_active = False

welcome_message = "\n<<<<<<<<<<<<<<<<<<< TICTACTOE >>>>>>>>>>>>>>>>>>> \n"
welcome_prompt = "Make a selection (Enter the selection number) \n"
welcome_options = """
    1. Start game
    2. Know the rules
    3. See previous scores
    4. Learn how the game works
    5. End program
    
    # Press Ctrl + C to end the program at any time \n
"""
welcome_screen_options = ["1", "2", "3", "4", "5"]

def display_tic_tac_toe_grid(grid_dictionary):
    """Prints the current state of the grid."""
    print("\n\n[TicTacToe Grid]")
    print(f"   {grid_dictionary['1']}   |   {grid_dictionary['2']}   |   {grid_dictionary['3']}   ")
    print("-------+-------+-------")
    print(f"   {grid_dictionary['4']}   |   {grid_dictionary['5']}   |   {grid_dictionary['6']}   ")
    print("-------+-------+-------")
    print(f"   {grid_dictionary['7']}   |   {grid_dictionary['8']}   |   {grid_dictionary['9']}   \n\n")

def reset_game_state():
    """Resets all variables for a new match."""
    global tic_tac_toe_grid, available_moves, played_moves, game_active
    tic_tac_toe_grid = {str(i): vacant_symbol for i in range(1, 10)}
    available_moves = [str(i) for i in range(1, 10)]
    played_moves = []
    game_active = True

def check_win(symbol):
    """Checks if the specific symbol has won."""
    for combo in winning_combinations:
        if all(tic_tac_toe_grid[pos] == symbol for pos in combo):
            return True
    return False

def check_draw():
    """Checks if the board is full."""
    return len(available_moves) == 0

def handle_move_update(move, symbol):
    """Updates the grid data and moves lists."""
    global available_moves, played_moves
    
    tic_tac_toe_grid[move] = symbol
    if move in available_moves:
        available_moves.remove(move)
    played_moves.append(move)

def get_user_move():
    """Gets validated input from the user."""
    print(f"Your turn ({opponent_symbol}). Available moves: {available_moves}")
    user_move_selection = input("Enter position number: ")

    while user_move_selection not in available_moves:
        print(f"Invalid selection. Please choose from: {available_moves}")
        user_move_selection = input("Enter position number: ")

    return user_move_selection

def get_smart_move(target_symbol):
    """
    Scans winning combinations to find a move that will complete a line 
    for the target_symbol (used for both winning and blocking).
    """
    for combo in winning_combinations:
        current_values = [tic_tac_toe_grid[pos] for pos in combo]
        
        # Check if line has 2 target symbols and 1 vacant spot
        if current_values.count(target_symbol) == 2 and current_values.count(vacant_symbol) == 1:
            # Find the empty position to return
            for pos in combo:
                if tic_tac_toe_grid[pos] == vacant_symbol:
                    return pos
    return None

def get_computer_move():
    """
    Decides the AI move based on priority:
    1. Win immediately
    2. Block opponent win
    3. Take Center
    4. Random available move
    """
    print("Computer is thinking...")
    
    # Priority 1: Check if Computer can win now
    winning_move = get_smart_move(computer_symbol)
    if winning_move:
        return winning_move

    # Priority 2: Check if Opponent needs to be blocked
    blocking_move = get_smart_move(opponent_symbol)
    if blocking_move:
        return blocking_move

    # Priority 3: Strategic center position
    if "5" in available_moves:
        return "5"

    # Priority 4: Random move
    return random.choice(available_moves)

def start_game():
    """Runs a single match until win or draw."""
    reset_game_state()
    display_tic_tac_toe_grid(tic_tac_toe_grid)
    
    while game_active:
        # --- PLAYER TURN ---
        opponent_move = get_user_move()
        handle_move_update(opponent_move, opponent_symbol)
        display_tic_tac_toe_grid(tic_tac_toe_grid)
        
        if check_win(opponent_symbol):
            print(">>> CONGRATULATIONS! You won! <<<\n")
            return # Exit function to go back to main menu
            
        if check_draw():
            print(">>> It's a DRAW! <<<\n")
            return

        # --- COMPUTER TURN ---
        computer_move = get_computer_move()
        handle_move_update(computer_move, computer_symbol)
        display_tic_tac_toe_grid(tic_tac_toe_grid)

        if check_win(computer_symbol):
            print(">>> GAME OVER. The Computer won! <<<\n")
            return
            
        if check_draw():
            print(">>> It's a DRAW! <<<\n")
            return

while True:
    print(welcome_message)
    print(welcome_prompt)
    print(welcome_options)

    selected_option = input("Selection: ")

    if selected_option not in welcome_screen_options:
        print("\n[ERROR] Invalid selection. Valid options are 1, 2, 3, 4, 5")
        continue

    if selected_option == "1":
        start_game()
    
    elif selected_option == "2":
        print("\n--- RULES ---")
        print("1. The game is played on a grid that's 3 squares by 3 squares.")
        print("2. You are X, your friend (or the computer) is O.")
        print("3. Players take turns putting their marks in empty squares.")
        print("4. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
        print("5. If all 9 squares are full and no one has 3 in a row, the game ends in a tie.\n")
        input("Press Enter to return to menu...")

    elif selected_option == "3":
        print("\n[Scores] Nope, We didn't work on this feature :( !\n")
        input("Press Enter to return to menu...")

    elif selected_option == "4":
        print("\n[Learning] Logic: The AI looks for wins first, then blocks, then takes center, then random.\n")
        input("Press Enter to return to menu...")

    elif selected_option == "5":
        print("Exiting program. Goodbye!")
        sys.exit()
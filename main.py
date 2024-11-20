# Initialize the Tic Tac Toe grid
grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display_grid():
    """Display the current state of the grid."""
    print(f" {grid[0]} | {grid[1]} | {grid[2]}")
    print("-----------")
    print(f" {grid[3]} | {grid[4]} | {grid[5]}")
    print("-----------")
    print(f" {grid[6]} | {grid[7]} | {grid[8]}")

def check_winner():
    """Check if there's a winner."""
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]
    for combo in winning_combinations:
        if grid[combo[0]] == grid[combo[1]] == grid[combo[2]]:
            return True
    return False

def is_draw():
    """Check if the game is a draw."""
    return all(cell in ["X", "O"] for cell in grid)

# Main game loop
print("Welcome to Tic Tac Toe!")
player_one = "X"
player_two = "O"
current_player = player_one

while True:
    display_grid()
    print(f"\nPlayer {current_player}'s turn.")
    try:
        position = int(input("Select your position (1-9): ")) - 1
        if grid[position] in ["X", "O"]:
            print("Position already taken. Choose another.")
            continue
    except (ValueError, IndexError):
        print("Invalid input. Please select a number between 1 and 9.")
        continue

    # Update the grid with the player's move
    grid[position] = current_player

    # Check for a winner or a draw
    if check_winner():
        display_grid()
        print(f"\nPlayer {current_player} wins!")
        break
    if is_draw():
        display_grid()
        print("\nIt's a draw!")
        break

    # Switch players
    current_player = player_two if current_player == player_one else player_one

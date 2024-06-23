import random

# Define constants
groceries = ['chicken', 'butter', 'milk', 'eggs', 'bread']
required_items = set(groceries)  # Set to store required items
player_position = (0, 0)  # Starting position of the player (Dawn)

# Store layout (simple grid)
store_layout = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
]

# Place items randomly in the store
for item in groceries:
    x = random.randint(0, len(store_layout) - 1)
    y = random.randint(0, len(store_layout[0]) - 1)
    store_layout[x][y] = item

# Function to simulate customer interaction
def customer_interaction():
    questions = [
        "Excuse me, where can I find the restrooms?",
        "How much are these donuts here?",
        "Do you have any discounts on milk today?",
        "Could you tell me where I can find the cooking oils?",
        "Is there a special offer on eggs this week?",
    ]
    question = random.choice(questions)
    print(f"Customer: {question}")

# Game loop
while True:
    # Display store layout
    for row in store_layout:
        print(' '.join(row))
    print()

    # Player's actions
    action = input("Enter your action (move, collect, help): ").strip().lower()

    if action == 'move':
        direction = input("Enter direction (north, south, east, west): ").strip().lower()
        # Move player
        if direction == 'north' and player_position[0] > 0:
            player_position = (player_position[0] - 1, player_position[1])
        elif direction == 'south' and player_position[0] < len(store_layout) - 1:
            player_position = (player_position[0] + 1, player_position[1])
        elif direction == 'east' and player_position[1] < len(store_layout[0]) - 1:
            player_position = (player_position[0], player_position[1] + 1)
        elif direction == 'west' and player_position[1] > 0:
            player_position = (player_position[0], player_position[1] - 1)
        else:
            print("Can't move in that direction!")
        
        # Check for customer interaction
        if random.random() < 0.3:  # 30% chance of encountering a customer
            print("You encounter a customer!")
            customer_interaction()
    
    elif action == 'collect':
        current_position = store_layout[player_position[0]][player_position[1]]
        if current_position in groceries:
            print(f"You collected {current_position}!")
            required_items.discard(current_position)
            store_layout[player_position[0]][player_position[1]] = '.'
            if not required_items:
                print("Congratulations! You've collected all the groceries.")
                break
        else:
            print("There's nothing to collect here.")

    elif action == 'help':
        print("Instructions: Move around using 'move' command (e.g., north, south, east, west).")
        print("Collect items using 'collect'.")
    
    else:
        print("Invalid command. Type 'help' for instructions.")

print("Game Over!")


import random

# #Welcome the player
def welcome_player():
    global player_name
    player_name = ""
    print("=== Welcome to the escape the castle game ===")
    print("Welcome to the game!")

 
    #Get player name, age and character class
    player_name=input("What is your name? ")
    age=int(input("How old are you? "))
    character_class=input("Choose a character class: ")
    
    #Set starting values
    health=100
    gold=50
    has_key=False
    
    #Display the character profile
    print("\n=== YOUR CHARACTER ===")
    print(f"Name: {player_name}")
    print(f"Age: {age}")
    print(f"Class: {character_class}")
    print(f"Health: {health}")
    print(f"Gold: {gold}")
    print(f"Has key: {has_key}")
    print(f"Inventory: []")
    
    #Begin the story
    print(f"\n{player_name}, you wake up in a dark spooky castle.")
    print("you hear ominous footsteps approaching. You must find a way to escape!")
    print("your adventure is about to begin. . . .")
    print("good luck!")


welcome_player()


# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================
 
# Create an inventory to store collected items
inventory = []
 
# Define the Cell scene
def cell():
    print("\nYou wake up in a dark castle cell.")
    print("You can see a door, a window and an old bed.")
 
# Create a variable to track whether the player has found the key
    has_key = False
 
# Repeat while the player has not found the key
    while has_key == False:
 
# Ask the player what to investigate
        choice = input("\nInvestigate the door, window or bed? "
        ).lower()
 
        if choice == "door":
            print("The door is locked.")
            print("You need to find a key")
 
        elif choice == "window":
            print("The window is barred. You can't escape that way.")
 
        elif choice == "bed":
            print("You look underneath the bed.")
            print("You find a small Iron Key")
 
# Add the key to the inventory
            inventory.append("Iron Key")
 
# Update the variable to stop the loop
            has_key = True
 
        else:
            print("Invalid choice. Please choose 'door', 'window', or 'bed'.")
 
# Code runs once the player has found the key.
print("\nYou unlock the cell door.")
print("You step out into the corridor.")
print(f"Your inventory: {inventory}")
 
 
# Start the scene
cell()



# ==========================================
# ESCAPE THE CASTLE - SCENE 2: THE CORRIDOR
# ==========================================
def corridor():
        print("\nYou walk down a dark castle corridor.")
        print("You hear a strange noise ahead...")
        # Create a list of possible encounters
        creatures = ["Guard", "Ghost", "vampire"]
    
        # Randomly select a creature
        random_creature = random.choice(creatures)
    
        # Pass the chosen creature into the encounter function
        encounter(random_creature)
    # Create a list to store the player's inventory
    # We are assuming the player already found the key
# Create a list to store the player's inventory
# We are assuming the player already found the key
inventory=["Iron Key"]
 
# Introduce the scene
print("You enter a long, dark corridor.")
print("You notice an old wooden cabinet.")
 
# Ask the player whether they want to open it
choice=input("Do you open the cabinet? yes/no: ").lower()
 
# If the player opens the cabinet...
if choice=="yes":
    print("You open the cabinet.")
    print("Inside, you find a Rusty Dagger!")
 
    # Add the dagger to the inventory list
    inventory.append("Rusty Dagger")
 
    print("You pick up the dagger.")
 
# If the player chooses anything other than yes...
else:
    print("You leave the cabinet closed.")
 
# Display all the items in the player's inventory
print(f"\nYour inventory: {inventory}")
 
# Check whether the dagger is in the inventory
if"Rusty Dagger"in inventory:
    print("You have a weapon to defend yourself!")
else:
    print("You don't have a weapon yet.")




#  ==========================================
#  ESCAPE THE CASTLE - CORRIDOR ENCOUNTER
#  ==========================================
 
# import random
 
# Define a function to describe an encounter
def encounter(creature):
    if creature == "Guard":
        print("The Guard draws their sword and blocks your path!")
    elif creature == "Ghost":
        print("A chilling ghost floats towards you, glowing in the dark! with the sound of chains rattling")
    elif creature == "vampire":
        print("A vampire swoops down from the shadows, fangs bared! dripping with blood")
        
    
    print(f"A wild {creature} appears!!")
 
# Define the corridor scene
 
    print("You walk down a dark castle corridor.")
    print("You hear a strange noise ahead...")
     # Create a list of possible encounters
creatures = ["Guard", "Ghost", "vampire"]
   
    # Randomly select a creature
random_creature = random.choice(creatures)
 
     # Pass the chosen creature into the encounter function
encounter(random_creature)
 
# Start the scene
corridor()

# ==========================================
# ESCAPE THE CASTLE - LIBRARY SCENE
# ==========================================

def library():
    print("\n--- SCENE: THE LIBRARY ---")
    print("You slip past the creature and slip into an old, dusty library.")
    print("A glowing ancient book rests on a pedestal. It reads:")
    print("'To pass the final gate, you must speak the word of power... freedom begins with F.'")
    
    # Let's add a quick interactive check or puzzle loop
    clue_found = False
    while not clue_found:
        action = input("Type 'read' to study the book further or 'leave' to move on: ").lower()
        if action == "read":
            print("You flip the pages. The password is whispered in your mind: 'FREEDOM'")
            clue_found = True
        elif action == "leave":
            print("You decide not to risk reading further and head towards the exit.")
            clue_found = True
        else:
            print("Please type 'read' or 'leave'.")
library()

# ==========================================
# ESCAPE THE CASTLE - FINAL SCENE: THE CASTLE GATE 
# ==========================================
def castle_gate():
    print("\n--- FINAL SCENE: THE CASTLE GATE ---")
    print("You reach the massive stone gates of the castle. This is your final obstacle.")
    print("A digital keypad blocks the mechanism. It asks for the password.")
    
    # Password guessing loop
    correct_password = "freedom"
    escaped = False
    
    while not escaped:
        guess = input("Enter the password (or type 'quit' to give up): ").lower()
        
        if guess == correct_password:
            print("\n✨ BEEP! The heavy lock clicks open! Green lights flash! ✨")
            print(f"CONGRATULATIONS, {player_name}! You have successfully escaped the castle!")
            escaped = True
        elif guess == 'quit':
            print("You stumble back in defeat. Game over!")
            break
        else:
            print("Access Denied! Incorrect password. Try again.")
castle_gate()

# ==========================================
# ESCAPE THE CASTLE - GAME FLOW
# ==========================================

def play_game():
    welcome_player()
    cell()
    corridor()
    library()
    castle_gate()

# Start the game
    play_game()
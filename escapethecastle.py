#Welcome the player
print("=== Welcome to the escape the castle game ===")
print("Welcome to the game!")
 
#Get player name, age and character class
player_name=input("What is your name? ")
age=int(input("How old are you? "))
character_class=input("Choose a character class: ")
 
#Set starting values
health=100
gold=50
haskey=False
 
#Display the character profile
print("\n=== YOUR CHARACTER ===")
print(f"Name: {player_name}")
print(f"Age: {age}")
print(f"Class: {character_class}")
print(f"Health: {health}")
print(f"Gold: {gold}")
print(f"Has Key: {haskey}")
 
#Begin the story
print(f"\n{player_name}, you wake up in a dark spooky castle.")
print("you hear ominous footsteps approaching. You must find a way to escape!")
print("your adventure is about to begin. . . .")
print("good luck!")


# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================
# Introduce the scene to the player
print ("you wake up in a dark, damp cell. The door is locked, and you can hear the sound of footsteps echoing through the castle.")
print("You can see a door, a window and an old bed")
# Ask the player what they want to investigate
# .lower() converts their answer to lowercase
choice = input("Do you want to investigate the door, window or bed?: ").lower()

choice = input("Do you want to investigate the door, window or bed?: ").lower()
 
# Check whether the player chose the door
if choice == "door":
    print("You walk towards the door.")
    print("You try the handle, but is it locked.")
 
# Check whether the player chose the window
elif choice == "window":
    print("You look through the window.")
    print("It is too small to escape through")
 
# Check whether the player chose the bed
elif choice == "bed":
    print("You look under the bed")
    print("You find a small Iron Key")
 
else:
    print("You decide not to investigate")


 #==========================================
# ESCAPE THE CASTLE - SCENE 2: THE HALLWAY
#==========================================

inventory = ["iron key"]  # Add the iron key to the player's inventory

#introduce the scene to the player


# Define a function with a creature parameter
def encounter(creature):
    print("You hear footsteps approaching...")
    print(f"A {creature} appears!")
    print("Prepare yourself!")
 
 
# Call the function with different arguments
encounter("Guard")
encounter("Ghost")
 
 
 
def encounter(creature):
 
    print(f"\nA {creature} appears!")
 
    # Add selection to respond to the creature
    if creature == "Guard":
        print("The guard draws their sword!")
 
    elif creature == "Ghost":
        print("The ghost floats towards you!")
    elif creature == "draugr":
        print("the draugr wakes up and slowly walks towards you")
# Test each possible encounter
encounter("Guard")
encounter("Ghost")
encounter("draugr")


# ==========================================
# ESCAPE THE CASTLE - CORRIDOR ENCOUNTER
# ==========================================
 
import random
 
# Define a function to describe an encounter
def encounter(creature):
 
        # Different outcomes depending on the creature
    if creature == "Guard":
        print("The Guard draws their sword")
    elif creature == "Ghost":
        print("The ghost floats towards")
    elif creature == "Sphinx":
        print("the Sphinx wakes up and slowly walks towards you")
 
    print(f"A {creature} appears!!")
 
# Define the corridor scene
def corridor():
    print("You walk down a dark castle corridor.")
    print("You hear a strange noise ahead...")
     # Create a list of possible encounters
    creatures = ["Guard", "Ghost", "Sphinx"]
   
    # Randomly select a creature
    random_creature = random.choice(creatures)
 
     # Pass the chosen creature into the encounter function
    encounter(random_creature)
 
# Start the scene
corridor()




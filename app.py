import streamlit as st
import random

# ==========================================
# 1. INITIALIZE GAME STATE (SESSION STATE)
# ==========================================
if "scene" not in st.session_state:
    st.session_state.scene = "start"
if "playerName" not in st.session_state:
    st.session_state.playerName = ""
if "playerClass" not in st.session_state:
    st.session_state.playerClass = "Warrior ⚔️"
if "health" not in st.session_state:
    st.session_state.health = 100
if "gold" not in st.session_state:
    st.session_state.gold = 50
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "strength" not in st.session_state:
    st.session_state.strength = 12
if "agility" not in st.session_state:
    st.session_state.agility = 10
if "intelligence" not in st.session_state:
    st.session_state.intelligence = 10
if "message" not in st.session_state:
    st.session_state.message = ""

# Display Game Title
st.title("Escape the Castle - Web Edition")

# ==========================================
# 2. DEFINE SCENE FUNCTIONS
# ==========================================

# SCENE 1: START / CHARACTER CREATION
def scene_start():
    st.header("=== Create Your Character ===")
    st.write("Welcome to Escape the Castle! Enter your details to begin your adventure.")
    
    name_input = st.text_input("What is your name?")
    class_input = st.selectbox("Choose your character class:", ["Warrior", "Mage", "Rogue", "Cleric"])
    
    if st.button("Start Adventure"):
        if name_input.strip() != "":
            st.session_state.playerName = name_input
            st.session_state.playerClass = class_input
            st.session_state.message = f"You wake up in a dark, cold cell, {name_input} the {class_input}."
            st.session_state.scene = "cell"  # Move to next scene
            st.rerun()  # Refresh page
        else:
            st.warning("Please enter your name first!")

# SCENE 2: THE DUNGEON CELL
def scene_cell():
    st.header("Room 1: The Dungeon Cell")
    st.write(st.session_state.message)
    
    if st.button("Search under the bed"):
        if "Iron Key" not in st.session_state.inventory:
            st.session_state.inventory.append("Iron Key")
            st.session_state.gold += 25
            st.session_state.message = "You search under the bed and find an Iron Key and 25 gold coins!"
            st.rerun()
        else:
            st.session_state.message = "There's nothing else under the bed."
            st.rerun()
            
    if st.button("Try the iron door"):
        if "Iron Key" in st.session_state.inventory:
            st.session_state.message = "You unlock the heavy iron door and step out into the dark corridor!"
            st.session_state.scene = "corridor"  # Move to Corridor
            st.rerun()
        else:
            st.session_state.message = "The door is locked tight. You need a key first!"
            st.rerun()
            
    if st.button("Check the window"):
        st.session_state.message = "The window is barred with iron. You can't escape that way."
        st.rerun()

# SCENE 3: THE CORRIDOR 
def scene_corridor():
    st.header("📍 The Dark Corridor")
    st.write(st.session_state.message)
    
    # ----------------------------------
    # OPTION 1: OPEN THE WOODEN CABINET
    # ----------------------------------
    if st.button("Open the old wooden cabinet"):
        if "Rusty Dagger" not in st.session_state.inventory:
            st.session_state.inventory.append("Rusty Dagger")
            st.session_state.message = (
                "You open the cabinet and find a Rusty Dagger! "
                "You pick it up."
            )
        else:
            st.session_state.message = (
                "The cabinet is already open and empty."
            )
        st.rerun()
        
    # ----------------------------------
    # OPTION 2: MOVE TO THE LIBRARY
    # ----------------------------------
    if st.button("Move forward to the Library"):
        st.session_state.scene = "library"  # Fixed from room to scene
        st.session_state.message = (
            "You slip past the corridor shadows "
            "into an old, dusty library."
        )
        st.rerun()

# SCENE 4: THE LIBRARY
def scene_library():
    st.header("Room 3: The Library")
    st.write(st.session_state.message)
    st.write("An ancient pedestal holds a glowing book: *'To pass the final gate, you must speak the word of power... freedom begins with F.'*")
    
    if st.button("Read ancient book"):
        st.session_state.message = "You flip the pages. The password is whispered in your mind: **FREEDOM**"
        st.rerun()
        
    if st.button("Head to Castle Gate"):
        st.session_state.message = "You reach the massive stone gates of the castle. A digital keypad blocks your exit."
        st.session_state.scene = "gate"  # Move to Gate
        st.rerun()

# SCENE 5: THE CASTLE GATE
def scene_gate():
    st.header("Final Scene: The Castle Gate")
    st.write(st.session_state.message)
    
    password = st.text_input("Enter the passcode:").lower()
    
    if st.button("Submit Password"):
        if password == "freedom":
            st.success(f"CONGRATULATIONS, {st.session_state.playerName}! You have escaped the castle!")
            st.balloons()
        else:
            st.error("Access Denied! Try again.")

# ==========================================
# 3. MAIN ROUTER / SCENE CONTROLLER
# ==========================================
if st.session_state.scene == "start":
    scene_start()
elif st.session_state.scene == "cell":
    scene_cell()
elif st.session_state.scene == "corridor":
    scene_corridor()
elif st.session_state.scene == "library":
    scene_library()
elif st.session_state.scene == "gate":
    scene_gate()

# ==========================================
# 4. SIDEBAR STATUS DISPLAY
# ==========================================
st.sidebar.subheader("Player Profile")
player_display = st.session_state.playerName if st.session_state.playerName else 'Anonymous'
st.sidebar.write(f"**Player:** {player_display}")
st.sidebar.write(f"**Class:** {st.session_state.playerClass}")
st.sidebar.markdown("---")
st.sidebar.subheader("Hero Attributes")
st.sidebar.write(f"Strength: {st.session_state.strength}")
st.sidebar.write(f"Agility: {st.session_state.agility}")
st.sidebar.write(f"Intelligence: {st.session_state.intelligence}")
st.sidebar.markdown("---")
st.sidebar.subheader("Live Status")
st.sidebar.write(f"Health: {st.session_state.health}/100")
st.sidebar.write(f"Gold Coins: {st.session_state.gold}")
st.sidebar.write(f"Inventory: {st.session_state.inventory}")
st.sidebar.write(f"Current Scene: {st.session_state.scene.capitalize()}")
st.sidebar.markdown("---")
if st.sidebar.button("Restart Game"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
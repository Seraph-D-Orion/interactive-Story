import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from google import genai
import random
 
load_dotenv(Path(__file__).resolve().with_name(".env"))
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
 
# ================================================================
# 1. PAGE SETUP — SAME APPROACH AS THE FINAL APP
# ================================================================
# page_icon uses the Unicode castle character, not an image file.
# Keep this before other Streamlit display calls.
 
st.set_page_config(page_title="Escape the Castle", page_icon="🏰", layout="centered")
st.title("🏰 Escape the Castle")
 
# ================================================================
# 2. GAME SETUP — INITIALISE VALUES ONCE
# ================================================================
# Session state remembers values when Streamlit reruns the script.
if "game_started" not in st.session_state:
    st.session_state.game_started = False
 
def start_game(name):
    """Set the same starting values and seven-room route as the final app."""
    st.session_state.game_started = True
    st.session_state.player_name = name
    st.session_state.health = 5
    st.session_state.max_health = 5
    st.session_state.inventory = ["Torch"]
    st.session_state.rooms = ["cell", "corridor", "library", "crypt", "guard_room", "dungeon", "castle_gate"]
    st.session_state.room_number = 0
    st.session_state.result_type = ""
    st.session_state.result_message = ""
    st.session_state.result_value = ""
    st.session_state.action_complete = False
 
 
def restart_game():
    st.session_state.clear()
    st.rerun()
 
def get_current_room():
    """Use the room number to find the name of the current room."""
    return st.session_state.rooms[st.session_state.room_number]
 
def continue_game():
    """Clear the last action and move to the next room."""
    st.session_state.result_type = ""
    st.session_state.result_message = ""
    st.session_state.result_value = ""
    st.session_state.action_complete = False
    st.session_state.room_number += 1
    st.rerun()
 
def add_item(item):
    if item not in st.session_state.inventory:
        st.session_state.inventory.append(item)
 
def has_item(item):
    return item in st.session_state.inventory
 
def remove_item(item):
    if item in st.session_state.inventory:
        st.session_state.inventory.remove(item)
 
def take_damage(amount):
    st.session_state.health = st.session_state.health - amount
    if st.session_state.health < 0:
        st.session_state.health = 0
 
def heal_player(amount):
    old_health = st.session_state.health
    st.session_state.health = min(st.session_state.max_health, st.session_state.health + amount)
    return st.session_state.health - old_health
 
def generate_story(room, action, outcome, fallback_message):
    if client is None:
        return fallback_message
 
    inventory_text = ", ".join(st.session_state.inventory)
 
    prompt = f"""
You are the storyteller for a grim, gothic dark fantasy
adventure game called Escape the Castle. The castle is ancient,
cursed, and hostile; even quiet moments should feel ominous.
 
Player: {st.session_state.player_name}
Room: {room}
Health: {st.session_state.health}/{st.session_state.max_health}
Inventory: {inventory_text}
 
Action:
{action}
 
Outcome:
{outcome}
 
Describe what happens in 30-50 words.
 
Use second person.
Use expicit atmospheric dark fantasy language.
Do not change the outcome.
Do not change health or inventory.
Do not introduce new choices.

"""
    try:
        interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
            generation_config={"thinking_level": "minimal"}
        )
        if interaction.output_text:
            return interaction.output_text
        return fallback_message
    except Exception as error:
        st.error(f"Gemini error: {error}")
        return fallback_message
 
def roll_dice():
    return random.randint(1,6)
 
def chance_encounter(button_text, room, action, success_number, success_outcome, success_fallback, failure_outcome, failure_fallback, damage, bonus_item=""):
    if st.button(button_text):
        roll = roll_dice()
        if bonus_item != "" and has_item(bonus_item):
            roll = roll + 2
        if roll >= success_number:
            story = generate_story(room, action, success_outcome, success_fallback)
            set_result("success", story)
        else:
            take_damage(damage)
            story = generate_story(room, action, failure_outcome, failure_fallback)
            set_result("damage", story, damage)
 
# ================================================================
# 3. REUSABLE DISPLAY FUNCTIONS — KEEP EVERY ROOM CONSISTENT
# ================================================================
 
def show_room(title, description):
    """Display a room heading and its description."""
    st.header(title)
    st.write(description)
 
def show_player_info():
    st.subheader(f"🧑 {st.session_state.player_name} ")
    left, right = st.columns(2)
    with left:
        st.write(f"❤️ Health: {st.session_state.health} / {st.session_state.max_health}")
    with right:
        st.write(f"🎒 Inventory: {', '.join(st.session_state.inventory)}")  
    st.caption(
        f"Room {st.session_state.room_number + 1}"
        f"of {len(st.session_state.rooms)}"
    )
    st.divider()
 
def set_result(result_type, message, value="Apple"):
    st.session_state.result_type = result_type
    st.session_state.result_message = message
    st.session_state.result_value = value
    st.session_state.action_complete = True
    st.rerun()
 
def show_result():
    # [UPDATE] Replace yesterday's show_result() with this whole function.
    kind = st.session_state.result_type
    value = st.session_state.result_value
 
    if kind == "item":
        st.success(f"🎒 NEW ITEM: {value}")
    elif kind == "damage":
        st.error(f"💔 DAMAGE: You lose {value} health.")
    elif kind == "heal":
        st.success(f"💚 HEALED: You recover {value} health.")
    elif kind == "success":
        st.success("✅ Success!")
    else:
        st.info("The journey continues...")
 
    st.write(st.session_state.result_message)
 
def show_continue_button(text = "Continue"):
    if st.button(text):
        continue_game()
 
# ================================================================
# 4. START SCREEN — NAME INPUT FROM DAY 1
# ================================================================
 
if not st.session_state.game_started:
 
    st.write("You wake beneath an ancient castle. Your goal is to escape.")
 
    name = st.text_input(
        "What is your name?",
        key="player_name_input"
    )
 
    if st.button("🏰 Enter the Castle", key="start_button"):
 
        if name.strip():
            st.session_state.game_started = True
            st.session_state.player_name = name.strip()
            st.session_state.health = 5
            st.session_state.max_health = 5
            st.session_state.inventory = ["Torch"]
            st.session_state.rooms = [
                "cell",
                "corridor",
                "crypt",
                "library",
                "guard_room",
                "dungeon",
                "castle_gate"
            ]
            st.session_state.room_number = 0
            st.session_state.result_type = ""
            st.session_state.result_message = ""
            st.session_state.result_value = ""
            st.session_state.action_complete = False
 
            st.rerun()
 
        else:
            st.warning("Please enter your name first!")
 
else:
    show_player_info()
    room = get_current_room()
 
    if st.session_state.health <= 0:
        show_room("💀 Game Over", "Your strength gives out. The castle has claimed another victim.")
        st.error("You did not escape the castle")
        if st.button("🔄 Try Again"):
            restart_game()
            st.stop()
 
    # ============================================================
    # ROOM 1 — CELL
    # ============================================================
    if room == "cell":
        show_room(
            "🔒 The Cell",
            "You wake on a cold stone floor of a prison cell. The iron door creaks open."
        )
        show_continue_button("🚪 Leave the cell")
 
    # ============================================================
    # ROOM 2 — CORRIDOR
    # ============================================================
    elif room == "corridor":
        show_room(
            "🕯️ The Corridor",
            "A wooden cabinet stands beside the staircase."
        )
 
        if not st.session_state.action_complete:
            left, right = st.columns(2)
 
            with left:
                if st.button("🔎 Search the cabinet"):
                    add_item("Rusty Dagger")
                    outcome = "The player searches the cabinet and finds a Rusty Dagger."
                    story = generate_story(
                        "The Corridor", "searching the wooden cabinet", outcome,
                        "Inside the cabinet, beneath a layer of dust and cobwebs, you find a Rusty Dagger."
                    )
                    set_result("item", story, "Rusty Dagger")
 
            with right:
                if st.button("➡️ Ignore it"):
                    outcome = "The player leaves the cabinet untouched and continues onwards."
                    story = generate_story(
                        "The Corridor", "ignoring the wooden cabinet", outcome,
                        "You leave the cabinet untouched and press on through the cold corridor."
                    )
                    set_result("story", story)
        else:
            show_result()
            show_continue_button()
 
    # ============================================================
    # ROOM 3 — CRYPT (LEARNERS REPEAT THE PATTERN)
    # ============================================================
    elif room == "crypt":
        show_room("⚰️ The Crypt", "A metal object glints beside a stone coffin.")
        if not st.session_state.action_complete:
            left, right = st.columns(2)
            with left:
                if st.button("🔎 Investigate"):
                    add_item("Iron Key")
                    outcome = "The player investigates the glinting object and safely takes the Iron Key."
                    story = generate_story(
                        "The Crypt", "investigating the metal object beside the stone coffin", outcome,
                        "Among the grave-dust, you find an Iron Key and close your fingers around its cold, pitted surface."
                    )
                    set_result("item", story, "Iron Key")
            with right:
                if st.button("🚪 Leave the crypt"):
                    outcome = "The player leaves the crypt without disturbing anything."
                    story = generate_story(
                        "The Crypt", "leaving the crypt undisturbed", outcome,
                        "You retreat from the coffin, leaving the dead to their silence."
                    )
                    set_result("story", story)
        else:
            show_result()
            show_continue_button()
 
    # ============================================================
    # ROOM 4 — LIBRARY (REPEAT THE PATTERN)
    # ============================================================
    elif room == "library":
        show_room("📚 The Forgotten Library", "A strange green light shines from an old book.")
        if not st.session_state.action_complete:
            left, right = st.columns(2)
            with left:
                if st.button("📖 Read the book"):
                    outcome = "The player reads the strange book; its pages glow with mysterious symbols."
                    story = generate_story(
                        "The Forgotten Library", "reading the strange green-lit book", outcome,
                        "The pages stir beneath your fingers, glowing with symbols that writhe like worms in the dark."
                    )
                    set_result("story", story)
            with right:
                if st.button("🚪 Leave it alone"):
                    outcome = "The player refuses to touch the book and leaves it alone."
                    story = generate_story(
                        "The Forgotten Library", "leaving the strange book untouched", outcome,
                        "You turn away from the book. Its sickly green light lingers at the edge of your vision."
                    )
                    set_result("story", story)
        else:
            show_result()
            show_continue_button()
 
    # ============================================================
    # ROOM 5 — GUARD ROOM (CHOICES WITHOUT DICE YET)
    # ============================================================
    elif room == "guard_room":
        show_room("⚔️ The Guard Room", "A ghostly knight blocks the doorway.")
        if "Rusty Dagger"  in st.session_state.inventory:
            st.info("⚔️ You are carrying a Rusty Dagger.")
        if not st.session_state.action_complete:
            left, right = st.columns(2)
            with left:
                if st.button("⚔️ Fight the knight"):
                    outcome = "The player defeats the knight and can continue."
                    story = generate_story(
                        "The Guard Room", "fight the ghostly knight", outcome, "You dodge the knight's sword. The armour crashes to the floor."
                    )
                    set_result("success", story)
                    st.rerun()
            with right:
                if st.button("🏃 Run past"):
                    outcome = "The player escapes past the knight without injury."
                    story = generate_story(
                        "The Guard Room", "running past the ghostly knight", outcome, "You sprint past the knight and escape through the doorway."
                    )
                    set_result("success", story)
                    st.rerun()
        else:
            show_result()
            show_continue_button()
 
    # ============================================================
    # ROOM 6 — DUNGEON (INVENTORY PERSISTS ACROSS ROOMS)
    # ============================================================
    #see a bottle of red liquid
    elif room == "dungeon":
        show_room(
            "🧪 The Dungeon",
            "You enter a dark, damp dungeon. "
            "On a stone table, you see a mysterious bottle "
            "filled with red liquid."
        )
        if not st.session_state.action_complete:
            left, right = st.columns(2)
            #left - take it, find a healing potion
            with left:
                if st.button("🧪 Take the bottle"):
                    add_item("Healing Potion")
                    outcome = "The player takes the red bottle and finds a Healing Potion."
                    story = generate_story(
                        "The Dungeon", "taking the bottle of red liquid from the stone table", outcome,
                        "You lift the bottle from the stone table. The red liquid shifts sluggishly inside: a Healing Potion."
                    )
                    set_result("item", story, "Healing Potion")
            #right - leave it, leave the bottle behind
            with right:
                if st.button("🚪 Leave it behind"):
                    outcome = "The player leaves the bottle behind and exits the dungeon."
                    story = generate_story(
                        "The Dungeon", "leaving the bottle of red liquid behind", outcome,
                        "You leave the bottle where it rests and withdraw from the damp chamber, its crimson contents still glimmering behind you."
                    )
                    set_result("story", story)
        else:
            show_result()
            show_continue_button()
 
    # ============================================================
    # ROOM 7 — CASTLE GATE (BRANCH BASED ON INVENTORY)
    # ============================================================
    elif room == "castle_gate":
        show_room(
            "🏰 The Castle Gate",
            "You finally reach the enormous castle gate. "
            "Beyond it lies freedom!"
        )
        #check to see if Iron Key held in inventory
        if "Iron Key" in st.session_state.inventory:
            st.success("🔑 You have the Iron Key!")
            #if key in inventory, show button to unlock the gate and escape
            if not st.session_state.action_complete:
                if st.button("🔓 Unlock the gate and escape"):
                    outcome = "The player uses the Iron Key to unlock the castle gate, steps outside, and escapes."
                    story = generate_story(
                        "The Castle Gate", "unlocking the gate with the Iron Key and stepping outside", outcome,
                        "The Iron Key turns with a tortured groan. The gate yields, and you cross its threshold into the bleak, open air beyond the castle."
                    )
                    set_result("success", story)
            else:
                show_result()
        #if no key in inventiory show button to climb the wall and escape
        else:
            st.info("🔒 You don't have the Iron Key!")
            if not st.session_state.action_complete:
                if st.button("🧗 Climb the wall and escape"):
                    outcome = "The player climbs the castle wall, drops safely onto the other side, and escapes."
                    story = generate_story(
                        "The Castle Gate", "climbing the castle wall to escape", outcome,
                        "You haul yourself over the jagged stones and drop safely beyond the walls. The castle looms behind you, silent and watchful."
                    )
                    set_result("success", story)
            else:
                show_result()
                st.header("🏆 YOU ESCAPED THE CASTLE!")
                st.balloons()
 
            st.divider()
            if st.button("🔄 Play Again"):
                restart_game()
                
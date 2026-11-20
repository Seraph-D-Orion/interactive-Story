# import os
# import random
# import streamlit as st
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=api_key) if api_key else None

# MODEL_NAME = "gemini-3.5-flash-lite"

# MAX_ENERGY = 5

# if "river_energy" not in st.session_state:
#     st.session_state.river_energy = MAX_ENERGY
# else:
#     st.session_state.river_energy = min(MAX_ENERGY, st.session_state.river_energy)

# if "water_ml" not in st.session_state:
#     st.session_state.water_ml = 600

# if "basic_shopping_list" not in st.session_state:
#     st.session_state.basic_shopping_list = []


# def roll_dice():
#     return random.randint(1, 6)


# def gain_energy(amount):
#     st.session_state.river_energy = min(MAX_ENERGY, st.session_state.river_energy + amount)


# def take_damage(amount):
#     st.session_state.river_energy = max(0, st.session_state.river_energy - amount)


# def add_item(item):
#     if item not in st.session_state.basic_shopping_list:
#         st.session_state.basic_shopping_list.append(item)
#     if item == "Energy Drink":
#         gain_energy(1)


# def has_item(item):
#     return item in st.session_state.basic_shopping_list


# def remove_item(item):
#     if item in st.session_state.basic_shopping_list:
#         st.session_state.basic_shopping_list.remove(item)


# def narrate_roll(scenario, outcome, roll, total, energy_left, fallback_text):
#     """Generates a 1-2 sentence adventure story beat using Gemini."""
#     if not client:
#         return fallback_text

#     prompt = (
#         f"You are a vivid, concise fantasy adventure narrator. "
#         f"Write 1 to 2 short sentences describing what happens next.\n"
#         f"Scenario: {scenario}\n"
#         f"Outcome: {outcome}\n"
#         f"Dice roll: {roll}, Total with gear: {total}\n"
#         f"Remaining energy: {energy_left}/{MAX_ENERGY}"
#     )

#     try:
#         response = client.models.generate_content(
#             model=MODEL_NAME,
#             contents=prompt,
#         )
#         text = (response.text or "").strip()
#         return text if text else fallback_text
#     except Exception:
#         return fallback_text


# st.write("You need a 4, 5 or 6 to cross a narrow bridge.")
# if st.button("🎲 Attempt the bridge"):
#     roll = roll_dice()
#     st.write(f"You rolled {roll}.")
#     if roll == 6:
#         st.success("Excellent! A perfect crossing!")
#         outcome = "Success (perfect crossing)"
#         fallback = "You step lightly across the weathered planks without a single wobble."
#     elif roll == 5:
#         st.success("Success! You crossed the bridge well.")
#         outcome = "Success (clean crossing)"
#         fallback = "Steady footing carries you across the swaying boards to the far bank."
#     elif roll == 4:
#         st.success("Success! You crossed the bridge safely.")
#         outcome = "Success (safe crossing)"
#         fallback = "A few boards creak beneath your boots, but you clear the drop safely."
#     elif roll == 3:
#         st.error("Failure! You tripped and twisted your ankle, return to the start.")
#         outcome = "Failure (tripped and twisted ankle, returned to start)"
#         fallback = "Your foot catches on a loose slat, sending you limping back to the trailhead."
#     elif roll == 2:
#         st.error("Failure! You fell from the bridge into water, return to the start.")
#         outcome = "Failure (fell from bridge into water, returned to start)"
#         fallback = "You lose your balance and splash into the cold water below before scrambling back."
#     else:
#         st.error("Failure! You died.")
#         outcome = "Failure (fatal fall)"
#         fallback = "The narrow span gives way in a flash, ending your trek over the gorge."

#     story = narrate_roll(
#         scenario="Narrow bridge over a chasm",
#         outcome=outcome,
#         roll=roll,
#         total=roll,
#         energy_left=st.session_state.river_energy,
#         fallback_text=fallback,
#     )
#     st.info(story)

# max_capacity = 1000
# water_left, water_right = st.columns(2)
# with water_left:
#     if st.button("💧 Refill 250 ml"):
#         st.session_state.water_ml = min(max_capacity, st.session_state.water_ml + 250)
# with water_right:
#     if st.button("🥤 Drink 250 ml"):
#         st.session_state.water_ml = max(0, st.session_state.water_ml - 250)

# st.write(f"Bottle: {st.session_state.water_ml}/{max_capacity} ml")

# st.header("🛒 Supply Shop")
# st.write("Buying an **Energy Drink** immediately restores +1 energy (up to a maximum of 5).")

# shop_options = ["Rope", "Bread", "Apples", "Water Bottle", "Climbing Boots", "Energy Drink"]

# for item in shop_options:
#     buy_col, check_col, return_col = st.columns(3)
#     with buy_col:
#         if st.button(f"Buy {item}"):
#             add_item(item)
#             if item == "Energy Drink":
#                 st.info("You drank an Energy Drink and gained +1 energy (capped at 5).")
#     with check_col:
#         if st.button(f"Check {item}"):
#             if has_item(item):
#                 st.success(f"{item} is on the list.")
#             else:
#                 st.warning(f"{item} is not on the list.")
#     with return_col:
#         if st.button(f"Put back {item}"):
#             remove_item(item)

# st.write("Current shopping list:", st.session_state.basic_shopping_list)


# def chance_encounter(
#     scenario_name,
#     success_number,
#     bonus_item="",
#     item_bonus=2,
#     success_message="Success! You made it through safely.",
#     failure_message="Failure! You stumble and lose energy.",
#     success_fallback="You push through the obstacle and steady your breath on the other side.",
#     failure_fallback="The terrain fights back, sapping your strength as you recover.",
# ):
#     roll = roll_dice()
#     bonus = item_bonus if (bonus_item != "" and has_item(bonus_item)) else 0
#     total = roll + bonus
#     st.write(f"Dice: {roll} | Equipment bonus: {bonus} | Total: {total}")

#     if total >= success_number:
#         st.success(success_message)
#         outcome = f"Success (needed {success_number}+)"
#         fallback = success_fallback
#     else:
#         energy_loss = 2 if roll in (1, 2) else 1
#         take_damage(energy_loss)
#         st.error(f"{failure_message} (Lost {energy_loss} energy.)")
#         outcome = f"Failure (needed {success_number}+, lost {energy_loss} energy)"
#         fallback = failure_fallback

#     story = narrate_roll(
#         scenario=scenario_name,
#         outcome=outcome,
#         roll=roll,
#         total=total,
#         energy_left=st.session_state.river_energy,
#         fallback_text=fallback,
#     )
#     st.info(story)


# st.header("🌊 River crossing")
# st.write("You can use **Rope** bought in the shop above. A Rope adds +2 to your dice roll.")
# st.write("A total of 4 or higher succeeds. Failing costs 2 energy on a roll of 1 or 2, or 1 energy otherwise.")

# if st.session_state.river_energy > 0:
#     if st.button("🌊 Attempt the river crossing"):
#         chance_encounter(
#             scenario_name="Swift river crossing",
#             success_number=4,
#             bonus_item="Rope",
#             item_bonus=2,
#             success_message="Success! You crossed the river safely.",
#             failure_message="Failure! You fall into the river.",
#             success_fallback="With your footing sure, you wade and haul yourself across the rushing current.",
#             failure_fallback=" icy spray surges around you as you fight the current back to shore.",
#         )
# else:
#     st.error("You have no energy left. Reset to try again.")

# st.header("⛰️ Steep mountain path")
# st.write("You can use **Climbing Boots** bought in the shop above. Climbing Boots add +1 to your dice roll.")
# st.write("A total of 5 or higher succeeds. Failing costs 2 energy on a roll of 1 or 2, or 1 energy otherwise.")

# if st.session_state.river_energy > 0:
#     if st.button("⛰️ Climb the steep mountain path"):
#         chance_encounter(
#             scenario_name="Steep rocky mountain path",
#             success_number=5,
#             bonus_item="Climbing Boots",
#             item_bonus=1,
#             success_message="Success! You climbed the steep mountain path safely.",
#             failure_message="Failure! You slip on the steep mountain path.",
#             success_fallback="Gripping handholds and jagged ledges, you crest the steep incline.",
#             failure_fallback="Loose scree shifts beneath your boots, forcing a tiring scramble to catch yourself.",
#         )
# else:
#     st.error("You have no energy left. Reset to try again.")

# if st.button("🔄 Reset energy"):
#     st.session_state.river_energy = MAX_ENERGY
#     st.rerun()

# st.write(f"Energy: {st.session_state.river_energy}/{MAX_ENERGY}")

import os
import random
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ================================================================
# 0. ENVIRONMENT & GEMINI NARRATIVE AI SETUP
# ================================================================
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
MODEL_NAME = "gemini-3.5-flash-lite"


def build_narrative_prompt(room_title, action, outcome):
    """Build a structured prompt so Gemini narrates an already-decided outcome."""
    inventory_text = ", ".join(st.session_state.inventory) if st.session_state.inventory else "Nothing"
    return f"""
Role: You are the narrative storyteller for a dark fantasy adventure game called Escape the Castle.
Player Name: {st.session_state.player_name}
Player Class: {st.session_state.player_class}
Current Room: {room_title}
Health: {st.session_state.health}/{st.session_state.max_health}
Inventory: {inventory_text}
Action Taken: {action}
Fixed Outcome: {outcome}

Constraints:
- Write in second person (you / your).
- Use atmospheric dark fantasy language.
- Keep the response between 35 and 60 words.
- Do not change the fixed outcome or add new choices.
- Do not invent new items or alter health/inventory rules.
- Return only the narrative description.
""".strip()


def narrate_event(room_title, action, outcome):
    """Return Gemini's narration for an event, falling back safely if needed."""
    if client is None:
        return outcome

    prompt = build_narrative_prompt(room_title, action, outcome)
    try:
        interaction = client.interactions.create(
            model=MODEL_NAME,
            input=prompt,
            generation_config={"thinking_level": "minimal"},
        )
        text = (interaction.output_text or "").strip()
        return text if text else outcome
    except Exception as error:
        st.caption(f"Note: Using fallback text ({type(error).__name__}).")
        return outcome


# ================================================================
# 1. PAGE SETUP
# ================================================================
st.set_page_config(page_title="Escape the Castle", page_icon="🏰", layout="centered")
st.title("🏰 Escape the Castle")


# ================================================================
# 2. GAME STATE & NAVIGATION HELPERS
# ================================================================
ROOMS = ["cell", "corridor", "crypt", "library", "guard_room", "dungeon", "castle_gate"]

ROOM_LABELS = {
    "cell": "🔒 The Cell",
    "corridor": "🕯️ The Corridor",
    "crypt": "⚰️ The Crypt",
    "library": "📚 The Forgotten Library",
    "guard_room": "🛡️ The Guard Room",
    "dungeon": "🧪 The Dusty Dungeon",
    "castle_gate": "🚪 The Castle Gate",
}


def start_game(name, player_class):
    """Initialize player stats, inventory, and room progression."""
    st.session_state.game_started = True
    st.session_state.player_name = name.strip()
    st.session_state.player_class = player_class
    st.session_state.health = 100
    st.session_state.max_health = 100
    st.session_state.gold = 50
    st.session_state.strength = 12
    st.session_state.agility = 10
    st.session_state.intelligence = 10
    st.session_state.inventory = ["Torch"]
    st.session_state.rooms = ROOMS
    st.session_state.room_number = 0
    st.session_state.result_type = ""
    st.session_state.result_message = ""
    st.session_state.result_value = ""
    st.session_state.action_complete = False
    st.session_state.game_over = False


def restart_game():
    """Reset all session state and return to the start screen."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


def get_current_room():
    """Return the active room key based on room_number."""
    return st.session_state.rooms[st.session_state.room_number]


def continue_game():
    """Clear current room result and move to the next room."""
    st.session_state.result_type = ""
    st.session_state.result_message = ""
    st.session_state.result_value = ""
    st.session_state.action_complete = False
    if st.session_state.room_number < len(st.session_state.rooms) - 1:
        st.session_state.room_number += 1
    st.rerun()


def add_item(item):
    """Add an item to inventory without duplicates."""
    if item not in st.session_state.inventory:
        st.session_state.inventory.append(item)


def adjust_health(amount):
    """Adjust health within [0, max_health] and flag defeat at 0."""
    st.session_state.health = max(0, min(st.session_state.max_health, st.session_state.health + amount))
    if st.session_state.health == 0:
        st.session_state.game_over = True


def set_result(result_type, message, value=""):
    """Store the outcome for the current room action and rerun."""
    st.session_state.result_type = result_type
    st.session_state.result_message = message
    st.session_state.result_value = value
    st.session_state.action_complete = True
    st.rerun()


# ================================================================
# 3. REUSABLE UI & SIDEBAR FUNCTIONS
# ================================================================
def show_sidebar():
    """Display live stats and a restart button in the sidebar."""
    st.sidebar.subheader("Player Profile")
    if not st.session_state.get("game_started"):
        st.sidebar.write("Not in game yet.")
        return

    current_room_key = get_current_room()
    st.sidebar.write(f"**Player:** {st.session_state.player_name}")
    st.sidebar.write(f"**Class:** {st.session_state.player_class}")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Hero Attributes")
    st.sidebar.write(f"Strength: {st.session_state.strength}")
    st.sidebar.write(f"Agility: {st.session_state.agility}")
    st.sidebar.write(f"Intelligence: {st.session_state.intelligence}")
    st.sidebar.markdown("---")
    st.sidebar.subheader("Live Status")
    st.sidebar.write(f"Health: {st.session_state.health}/{st.session_state.max_health}")
    st.sidebar.write(f"Gold Coins: {st.session_state.gold}")
    st.sidebar.write(f"Inventory: {', '.join(st.session_state.inventory)}")
    st.sidebar.write(f"Current Room: {ROOM_LABELS[current_room_key]}")
    st.sidebar.markdown("---")
    if st.sidebar.button("Restart Game", key="sidebar_restart"):
        restart_game()


def show_player_info():
    """Display top-of-screen player summary bar."""
    st.subheader(f"🧑 {st.session_state.player_name} ({st.session_state.player_class})")
    left, right = st.columns(2)
    with left:
        st.write(f"❤️ Health: {st.session_state.health}/{st.session_state.max_health}")
        st.write(f"🪙 Gold: {st.session_state.gold}")
    with right:
        st.write(f"🎒 Inventory: {', '.join(st.session_state.inventory)}")
        st.caption(f"Room {st.session_state.room_number + 1} of {len(st.session_state.rooms)}")
    st.divider()


def show_room(title, description):
    """Display room heading and intro text."""
    st.header(title)
    st.write(description)


def show_result():
    """Display the stored result message after an action."""
    kind = st.session_state.result_type
    message = st.session_state.result_message
    if kind == "item":
        st.success(f"🎒 NEW ITEM: {st.session_state.result_value}")
        st.write(message)
    elif kind == "success":
        st.success(message)
    elif kind == "warning":
        st.warning(message)
    else:
        st.info(message)


def show_continue_button(text="Continue"):
    """Render button to move to the next room."""
    if st.button(text):
        continue_game()


# ================================================================
# 4. START SCREEN & MAIN ROOM ROUTER
# ================================================================
if "game_started" not in st.session_state:
    st.session_state.game_started = False

show_sidebar()

if not st.session_state.game_started:
    st.write("You wake beneath an ancient castle. Your goal is to escape.")
    name_input = st.text_input("What is your name?")
    class_input = st.selectbox("Choose your character class:", ["Warrior", "Mage", "Rogue", "Cleric"])

    if st.button("Enter the Castle"):
        if name_input.strip():
            start_game(name_input, class_input)
            st.rerun()
        else:
            st.warning("Enter your name first before starting.")
else:
    show_player_info()
    room = get_current_room()

    if st.session_state.game_over:
        st.error("💀 You have fallen in the depths of the castle. Your journey ends here.")
        if st.button("Try Again"):
            restart_game()
    else:
        # --------------------------------------------------------
        # ROOM 1 — CELL
        # --------------------------------------------------------
        if room == "cell":
            show_room("🔒 The Cell", "You wake on a cold stone floor. The iron door creaks open.")
            show_continue_button("🚪 Leave the cell")

        # --------------------------------------------------------
        # ROOM 2 — CORRIDOR
        # --------------------------------------------------------
        elif room == "corridor":
            show_room("🕯️ The Corridor", "A wooden cabinet stands beside the staircase.")
            if not st.session_state.action_complete:
                left, right = st.columns(2)
                with left:
                    if st.button("🔎 Search the cabinet"):
                        add_item("Rusty Dagger")
                        st.session_state.gold += 10
                        outcome = "You search the cabinet, collect 10 gold coins, and find a Rusty Dagger."
                        story = narrate_event("The Corridor", "Search the wooden cabinet", outcome)
                        set_result("item", story, "Rusty Dagger")
                with right:
                    if st.button("➡️ Ignore it"):
                        outcome = "You leave the cabinet untouched and move toward the stairs."
                        story = narrate_event("The Corridor", "Ignore the cabinet", outcome)
                        set_result("story", story)
            else:
                show_result()
                show_continue_button()

        # --------------------------------------------------------
        # ROOM 3 — CRYPT
        # --------------------------------------------------------
        elif room == "crypt":
            show_room("⚰️ The Crypt", "A metal object glints beside a stone coffin.")
            if not st.session_state.action_complete:
                left, right = st.columns(2)
                with left:
                    if st.button("🔎 Investigate the coffin"):
                        add_item("Iron Key")
                        outcome = "You carefully search beside the stone coffin and claim an Iron Key."
                        story = narrate_event("The Crypt", "Investigate beside the stone coffin", outcome)
                        set_result("item", story, "Iron Key")
                with right:
                    if st.button("➡️ Leave it alone"):
                        outcome = "You leave the stone coffin undisturbed and press onward."
                        story = narrate_event("The Crypt", "Leave the coffin alone", outcome)
                        set_result("story", story)
            else:
                show_result()
                show_continue_button()

        # --------------------------------------------------------
        # ROOM 4 — LIBRARY
        # --------------------------------------------------------
        elif room == "library":
            show_room("📚 The Forgotten Library", "A strange pulsing green light shines from an old book.")
            if not st.session_state.action_complete:
                left, right = st.columns(2)
                with left:
                    if st.button("📖 Investigate the glowing book"):
                        add_item("Library Clue")
                        outcome = "You open the glowing book and uncover the secret word: FREEDOM."
                        story = narrate_event("The Forgotten Library", "Read the glowing book", outcome)
                        set_result("item", story, "Library Clue")
                with right:
                    if st.button("➡️ Walk away"):
                        outcome = "You ignore the green glow and hurry past the bookshelves."
                        story = narrate_event("The Forgotten Library", "Walk away from the book", outcome)
                        set_result("story", story)
            else:
                show_result()
                show_continue_button()

        # --------------------------------------------------------
        # ROOM 5 — GUARD ROOM
        # --------------------------------------------------------
        elif room == "guard_room":
            show_room("🛡️ The Guard Room", "An armored sentry patrols the doorway ahead.")
            if not st.session_state.action_complete:
                left, right = st.columns(2)
                with left:
                    if st.button("🤫 Slip past quietly"):
                        if random.random() < 0.65:
                            outcome = "You slip past the sentry in the shadows without taking a scratch."
                            story = narrate_event("The Guard Room", "Sneak past the guard", outcome)
                            set_result("success", story)
                        else:
                            adjust_health(-20)
                            outcome = "A loose stone clatters; the guard strikes you for 20 health before you slip through."
                            story = narrate_event("The Guard Room", "Sneak past the guard (caught)", outcome)
                            set_result("warning", story)
                with right:
                    if st.button("⚔️ Slip past briskly"):
                        adjust_health(-15)
                        outcome = "You dash past the guard and take a glancing blow for 15 health, but make it through."
                        story = narrate_event("The Guard Room", "Dash past the guard", outcome)
                        set_result("warning", story)
            else:
                show_result()
                if not st.session_state.game_over:
                    show_continue_button()

        # --------------------------------------------------------
        # ROOM 6 — DUSTY DUNGEON
        # --------------------------------------------------------
        elif room == "dungeon":
            show_room("🧪 The Dusty Dungeon", "A bottle of red liquid rests on a stone pedestal.")
            if not st.session_state.action_complete:
                left, right = st.columns(2)
                with left:
                    if st.button("🧪 Drink the red potion"):
                        add_item("Healing Potion")
                        adjust_health(25)
                        outcome = "You drink the red healing potion and restore 25 health."
                        story = narrate_event("The Dusty Dungeon", "Drink the red potion", outcome)
                        set_result("item", story, "Healing Potion")
                with right:
                    if st.button("➡️ Leave it behind"):
                        outcome = "You leave the bottle on the pedestal and head toward the final gate."
                        story = narrate_event("The Dusty Dungeon", "Leave the potion behind", outcome)
                        set_result("story", story)
            else:
                show_result()
                show_continue_button()

        # --------------------------------------------------------
        # ROOM 7 — CASTLE GATE
        # --------------------------------------------------------
        elif room == "castle_gate":
            show_room("🚪 The Castle Gate", "Towering iron gates stand between you and freedom.")
            if not st.session_state.action_complete:
                has_key = "Iron Key" in st.session_state.inventory
                if has_key:
                    st.info("You carry the **Iron Key** from the crypt.")
                else:
                    st.info("You do not have the **Iron Key**.")

                passcode = st.text_input("Enter the secret word (if you know it):").strip().lower()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔓 Unlock & Escape"):
                        if has_key and passcode == "freedom":
                            outcome = "With the Iron Key and the word FREEDOM, the heavy gates swing open into the night air."
                            story = narrate_event("The Castle Gate", "Unlock gates with Iron Key and word FREEDOM", outcome)
                            st.balloons()
                            set_result("success", f"🎉 {story}")
                        elif has_key:
                            outcome = "The Iron Key turns, but a rune lock still bars the gate until you speak the right word."
                            story = narrate_event("The Castle Gate", "Try gate without the secret word", outcome)
                            set_result("warning", story)
                        else:
                            outcome = "Without the Iron Key, the lock holds firm against your efforts."
                            story = narrate_event("The Castle Gate", "Try gate without Iron Key", outcome)
                            set_result("warning", story)

                with col2:
                    if st.button("🧗 Climb the outer wall"):
                        adjust_health(-15)
                        if not st.session_state.game_over:
                            outcome = f"You scale the rough castle wall, losing 15 health (now {st.session_state.health}), and escape into freedom."
                            story = narrate_event("The Castle Gate", "Climb the castle wall to escape", outcome)
                            st.balloons()
                            set_result("success", f"🧗 {story}")
            else:
                show_result()
                st.markdown("---")
                if st.button("Play Again 🔄"):
                    restart_game()
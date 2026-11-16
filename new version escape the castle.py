import streamlit as st

st.title("Escape the Castle - Web Edition")

# 1. Initialize Game Memory (Session State)
if "room" not in st.session_state:
    st.session_state.room = "cell"
if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "health" not in st.session_state:
    st.session_state.health = 100
if "message" not in st.session_state:
    st.session_state.message = "You wake up in a dark castle cell. You can see a door, a window, and an old bed."

# 2. Room 1: The Cell Scene
if st.session_state.room == "cell":
    st.header("📍 The Dungeon Cell")
    st.write(st.session_state.message)

    if st.button("Search under the bed"):
        if "Iron Key" not in st.session_state.inventory:
            st.session_state.inventory.append("Iron Key")
            st.session_state.message = "You look underneath the bed and find a small Iron Key! 🔑"
        else:
            st.session_state.message = "You already searched under the bed. There is nothing else here."

    if st.button("Try the door"):
        if "Iron Key" in st.session_state.inventory:
            st.session_state.room = "corridor"
            st.session_state.message = "You unlock the cell door with your Iron Key and step into the dark corridor!"
        else:
            st.session_state.message = "The door is locked tight. You need to find a key first!"

    if st.button("Check the window"):
        st.session_state.message = "The window is barred with iron. You can't escape that way."

# 3. Room 2: The Corridor Scene
elif st.session_state.room == "corridor":
    st.header("📍 The Dark Corridor")
    st.write(st.session_state.message)

    if st.button("Open the old wooden cabinet"):
        if "Rusty Dagger" not in st.session_state.inventory:
            st.session_state.inventory.append("Rusty Dagger")
            st.session_state.message = "You open the cabinet and find a Rusty Dagger! 🗡️ You pick it up."
        else:
            st.session_state.message = "The cabinet is already open and empty."

    if st.button("Move forward to the Library"):
        st.session_state.room = "library"
        st.session_state.message = "You slip past the corridor shadows into an old, dusty library."

# 4. Room 3: The Library Scene
elif st.session_state.room == "library":
    st.header("📍 The Library")
    st.write(st.session_state.message)
    st.write("A glowing ancient book rests on a pedestal: *'To pass the final gate, you must speak the word of power... freedom begins with F.'*")

    if st.button("Read the ancient book"):
        st.session_state.message = "You flip the pages. The password is whispered in your mind: **FREEDOM**"

    if st.button("Head to the Castle Gate"):
        st.session_state.room = "gate"
        st.session_state.message = "You reach the massive stone gates of the castle. A digital keypad blocks your exit."

# 5. Final Scene: The Castle Gate
elif st.session_state.room == "gate":
    st.header("📍 The Castle Gate")
    st.write(st.session_state.message)
    
    # Text input for password guessing in Streamlit
    password_guess = st.text_input("Enter the password:").lower()
    
    if st.button("Submit Password"):
        if password_guess == "freedom":
            st.success("✨ BEEP! The heavy lock clicks open! Green lights flash! You have successfully escaped the castle! 🎉")
        else:
            st.error("❌ Access Denied! Incorrect password. Try again.")

# 🎒 Sidebar to Display Player Status Live
st.sidebar.subheader("Player Status")
st.sidebar.write(f"❤️ Health: {st.session_state.health}")
st.sidebar.write(f"🎒 Inventory: {st.session_state.inventory}")

# 🏰 Escape the Castle — Streamlit & Gemini AI Adventure

An interactive, choice-based dark fantasy web adventure built with **Python**, **Streamlit**, and the **Google GenAI SDK**. 

This repository contains the complete 7-room web app code for *Escape the Castle*. It is structured to maintain game state, track player inventory and health, and dynamically enrich room outcomes using Gemini AI narration.

---

## 🌟 Key Features

* **Persistent Game State (`st.session_state`):** Tracks player progress, health ($5/5$), inventory items, active room index, and action resolution without losing data across browser reruns.
* **Modular 7-Room Campaign:** Linear route through interconnected gothic environments with room-specific choices and inventory checks.
* **AI Narrative Integration (`google-genai`):** Dynamic storytelling powered by `gemini-3.5-flash-lite`, generating dark fantasy descriptions tailored to the player's name, room, and action while enforcing strict outcome fallbacks.
* **Reusable UI Components:** Standardized display helpers (`show_room`, `show_player_info`, `show_result`, `show_continue_button`) for a clean, consistent interface.
* **Branching & Victory Conditions:** Multiple resolution pathways at the castle gate based on whether the player acquired key items.

---

## 🗺️ Campaign Structure

| Room Number | Room Title | Key Actions & Mechanics |
| :--- | :--- | :--- |
| **Room 1** | 🔒 The Cell | Waking up, opening door, initializing state |
| **Room 2** | 🕯️ The Corridor | Cabinet search $\rightarrow$ Obtain **Rusty Dagger** |
| **Room 3** | ⚰️ The Crypt | Coffin investigation $\rightarrow$ Obtain **Iron Key** |
| **Room 4** | 📚 The Forgotten Library | Reading glowing book $\rightarrow$ Narrative clue |
| **Room 5** | ⚔️ The Guard Room | Ghostly knight encounter $\rightarrow$ Combat / Stealth |
| **Room 6** | 🧪 The Dungeon | Table investigation $\rightarrow$ Obtain **Healing Potion** |
| **Room 7** | 🏰 The Castle Gate | Final escape check (Iron Key unlock vs. Wall climb) |

---

## 📁 File Structure

```text
escape-the-castle/
├── app.py              # Main Streamlit application file
├── .env                # Local environment variables (GEMINI_API_KEY)
├── .gitignore          # Keeps secrets and environment files out of Git
├── README.md           # Project documentation and guide
└── requirements.txt    # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.10+** installed on your machine.
* A **Google Gemini API Key** (optional, fallback descriptions will display if omitted).

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install Dependencies

Create and activate a virtual environment (optional but recommended), then install required packages:

```bash
pip install streamlit python-dotenv google-genai
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of your project:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> **Note:** Ensure `.env` is listed in your `.gitignore` file so your API key is never exposed publicly.

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

Your browser will automatically open the web application at `http://localhost:8501`.

---

## 🛠️ Using This Code as an Independent Project Template

This codebase is designed as a reusable pattern for building choice-based Streamlit games:

1. **Adding New Rooms:** Update the `st.session_state.rooms` list inside `start_game()` and add corresponding `elif room == "your_room_name":` blocks.
2. **Modifying AI Narratives:** Customize `generate_story()` to adjust the tone, persona, constraints, or storytelling style.
3. **Adding Dice / Chance Encounters:** Utilize the built-in `chance_encounter()` and `roll_dice()` helper functions for risk-reward mechanics.
4. **Custom Player Stats:** Extend `start_game()` to track additional attributes like Gold, Mana, or Special Abilities.

---

## 📜 License

This project was built as part of the *Level 2 Coding with AI Assistant* course. Feel free to fork, adapt, and build upon this template for independent projects!

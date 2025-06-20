# 🎮 Streamlit Multi-Game App

This is a **Streamlit-based web application** that combines **three mini-games**:
- **Tic Tac Toe**
- **Magic 8 Ball**
- **Rock Paper Scissors**

---

## 🛠 Features

- 🧠 **Magic 8 Ball** — Get random predictive answers.
- ✊ **Rock Paper Scissors** — Play against the computer.
- ❌ **Tic Tac Toe** — Play a single-player game vs. computer.

---

## 📂 File Structure

```plaintext
.
├── app.py           # Main Streamlit app
├── project.py       # Game logic
├── test.py          # Unit tests
└── README.md        # This file
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/streamlit-mini-games.git
   cd streamlit-mini-games
   ```

2. Install dependencies:
   ```bash
   pip install streamlit
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 📘 Function-by-Function Breakdown

### `app.py`
This is the entry point of the Streamlit app.

- **`st.sidebar.radio(...)`**: Lets the user choose which game to play.
- Based on user selection, calls the appropriate function from `project.py`.

---

### `project.py`
This file contains the game logic.

#### ✅ Rock Paper Scissors
```python
def RockPaperScissors()
```
- Lets the user pick rock, paper, or scissors.
- Randomly chooses the computer's move.
- Displays result based on the `is_win()` logic.

```python
def is_win(player, player2)
```
- Returns `True` if `player` beats `player2`.
- Used to determine game outcomes.

---

#### ✅ Magic 8 Ball
```python
def MagicBall()
```
- Picks a random number between 1 and 9.
- Shows a corresponding fortune response.

---

#### ✅ Tic Tac Toe
```python
def TicTacToe()
```
- Initializes game state using Streamlit session.
- Alternates between player `'X'` and computer `'O'`.
- Renders buttons for each board position.
- Checks for win/draw using helper functions.

---

### Helper Functions

```python
def DefineBoard()
```
- Initializes a 3x3 board as a dictionary with keys 1–9.

```python
def UpdateBoard(board, player, position)
```
- Updates the board at `position` with `player`'s symbol.

```python
def CheckSpot(board, position)
```
- Returns `True` if a position is empty.

```python
def Winner(board, player)
```
- Checks all 8 possible win conditions.
- Returns `True` if the given player has won.

```python
def checkFullBoard(board)
```
- Returns `True` if all positions are filled (draw).

```python
def DisplayBoard(board)
```
- Returns a string-based visual representation of the board.

---

## 🧪 Testing

Basic tests are located in `test.py` and include:
- Validating game logic (win conditions)
- Board updates
- Display formatting
- Spot availability

---

## 📄 License

```
MIT License

Copyright (c) 2025 Dinesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND.
```

---

## 👨‍💻 Author

**Dinesh** – Developer of this multi-game Streamlit application.  
For feedback or collaboration, feel free to connect!

---

## 💡 Future Improvements

- Add two-player online support for Tic Tac Toe
- Maintain user scores across games
- Add animations and sound effects

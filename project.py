import streamlit as st
import random

def getGame():
    pass  # Not needed in Streamlit, kept for compatibility

def RockPaperScissors():
    user = st.radio("Choose:", ['Rock (r)', 'Paper (p)', 'Scissors (s)'])
    if st.button("Play"):
        user_choice = user[0].lower()
        computer = random.choice(['r', 'p', 's'])
        st.write(f"Computer chose: **{computer.upper()}**")
        if user_choice == computer:
            st.info("You tied!")
        elif is_win(user_choice, computer):
            st.success("You won!")
        else:
            st.error("You lost!")

def is_win(player, player2):
    return (player == 'r' and player2 == 's') or \
           (player == 's' and player2 == 'p') or \
           (player == 'p' and player2 == 'r')

def MagicBall():
    if st.button("Ask the Magic Ball"):
        responses = {
            1: 'It is certain',
            2: 'It is decidedly so',
            3: 'Yes',
            4: 'Reply hazy try again',
            5: 'Ask again later',
            6: 'Concentrate and ask again',
            7: 'My reply is no',
            8: 'Outlook not so good',
            9: 'Very doubtful'
        }
        result = random.randint(1, 9)
        st.info(f"Magic 8 Ball says: **{responses[result]}**")

def TicTacToe():
    if 'board' not in st.session_state:
        st.session_state.board = DefineBoard()
        st.session_state.current = 'X'
        st.session_state.winner = None

    board = st.session_state.board
    current = st.session_state.current

    cols = st.columns(3)
    for i in range(1, 10):
        col = cols[(i - 1) % 3]
        with col:
            if st.button(board[i] if board[i] != ' ' else str(i), key=i):
                if board[i] == ' ' and not st.session_state.winner:
                    UpdateBoard(board, current, i)
                    if Winner(board, current):
                        st.session_state.winner = current
                    elif checkFullBoard(board):
                        st.session_state.winner = 'Draw'
                    else:
                        st.session_state.current = 'O' if current == 'X' else 'X'

    st.text(DisplayBoard(board))

    if st.session_state.winner:
        if st.session_state.winner == 'Draw':
            st.warning("It's a Draw!")
        else:
            st.success(f"{st.session_state.winner} wins!")

        if st.button("Restart Game"):
            st.session_state.board = DefineBoard()
            st.session_state.current = 'X'
            st.session_state.winner = None

def DefineBoard():
    return {i: ' ' for i in range(1, 10)}

def UpdateBoard(board, player, position):
    board[int(position)] = player

def CheckSpot(board, position):
    return board[int(position)] == ' '

def Winner(board, player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def checkFullBoard(board):
    return all(value != ' ' for value in board.values())

def DisplayBoard(board):
    return (f'{board[1]}|{board[2]}|{board[3]}   1 2 3\n'
            f'-----\n'
            f'{board[4]}|{board[5]}|{board[6]}   4 5 6\n'
            f'-----\n'
            f'{board[7]}|{board[8]}|{board[9]}   7 8 9')

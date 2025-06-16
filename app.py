import streamlit as st
import random

from project import getGame, RockPaperScissors, MagicBall, TicTacToe

st.title("🎮 Welcome to Streamlit Games")

game = st.sidebar.radio("Choose a game:", ["Tic Tac Toe", "Magic 8 Ball", "Rock Paper Scissors"])

if game == "Rock Paper Scissors":
    st.subheader("✊ Rock Paper Scissors")
    RockPaperScissors()

elif game == "Magic 8 Ball":
    st.subheader("🎱 Magic 8 Ball")
    MagicBall()

elif game == "Tic Tac Toe":
    st.subheader("❌ Tic Tac Toe")
    TicTacToe()

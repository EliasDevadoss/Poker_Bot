import streamlit as st
from card_deck import CardDeck
from chips import Chips
import display_game
import openai
import opponent_move
import random


# Header
st.title("Poker 🃟 Bot.")
st.write(
    "Welcome to the minimalist Poker Bot. Designed by Elias Devadoss."
)

# Initializes the deck of cards, as well as the board and hands
if 'deck' not in st.session_state:
    st.session_state.deck = CardDeck()
flop = st.session_state.deck.get_flop()
turn = st.session_state.deck.get_turn()
river = st.session_state.deck.get_river()
hero_hand = st.session_state.deck.get_hero()
villain_hand = st.session_state.deck.get_villain()

# Initializes user stacks and pot
if 'chips' not in st.session_state:
    st.session_state.chips = Chips()
hero_stack = st.session_state.chips.get_hero()
villain_stack = st.session_state.chips.get_villain()
pot = st.session_state.chips.get_pot()

# Initializes button
if 'btn' not in st.session_state:
    if random.random() < 0.5:
        st.session_state.btn = True # Hero on button
    else:
        st.session_state.btn = False # Villain on button

# Initializes the board to hidden
if 'flop' not in st.session_state:
    st.session_state.flop = False
if 'turn' not in st.session_state:
    st.session_state.turn = False
if 'river' not in st.session_state:
    st.session_state.river = False

# Displays the hands and board
display_game.display_players(hero_hand, villain_hand, st.session_state.btn)
display_game.display_chips(hero_stack, villain_stack, pot)
st.divider()
display_game.display_board(flop, turn, river)

# Shows user options dependent on opponent bet
bet = st.slider("Bet size:", 0, hero_stack, 0)

facing_bet = False
if(facing_bet==False):
    options = ["Check", "Bet " + bet]
else:
    options = ["Fold", "Call", "Raise 3x"]
st.radio("Your action:", options, horizontal=True)

confirm = st.button("Confirm")
if confirm:
    st.session_state.flop = True
    st.rerun()

# Decides villain move
opponent_move.callAI(flop, turn, river, villain_hand)

# Resets entire game to a new hand
reset = st.button("New Hand", type="primary")
if reset:
    st.session_state.deck = CardDeck()
    st.session_state.chips = Chips()
    st.session_state.flop = False
    st.session_state.turn = False
    st.session_state.river = False
    if random.random() < 0.5:
        st.session_state.btn = True # Hero on button
    else:
        st.session_state.btn = False # Villain on button
    st.rerun()

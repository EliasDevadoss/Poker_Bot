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
if 'facing_bet' not in st.session_state:
    st.session_state.facing_bet = False
if 'action' not in st.session_state: # Who the current action is on. Starts off-dealer
    st.session_state.action = not st.session_state.btn

# Initializes the board to hidden
if 'flop' not in st.session_state:
    st.session_state.flop = False
if 'turn' not in st.session_state:
    st.session_state.turn = False
if 'river' not in st.session_state:
    st.session_state.river = False
if 'game_end' not in st.session_state:
    st.session_state.game_end = False

if st.session_state.game_end:
    st.session_state.flop = True
    st.session_state.turn = True
    st.session_state.river = True

# Displays the hands and board
display_game.display_players(hero_hand, villain_hand, st.session_state.btn)
display_game.display_chips(hero_stack, villain_stack, pot)
st.divider()
display_game.display_board(flop, turn, river)

# Shows user options dependent on opponent bet
if hero_stack > 0:
    bet = st.slider("Bet size:", 0, hero_stack, 0)
else:
    bet = 0

if st.session_state.facing_bet:
    callText = "Call " + str(st.session_state.chips.get_villain_bet())
    options = ["Fold", callText, "Raise 3x"]
else:
    options = ["Check", "Bet " + str(bet)]
choice = st.radio("Your action:", options, horizontal=True)

confirm = st.button("Confirm")

if not st.session_state.action and not st.session_state.game_end: # Not hero's turn
    opponent_move.takeTurn(flop, turn, river, villain_hand)
elif confirm and not st.session_state.game_end:
    villRaise = False
    if choice == "Check":
        st.session_state.action = False
        st.rerun()
        villRaise = opponent_move.takeTurn(flop, turn, river, villain_hand)
    elif choice[:3] == "Bet":
        st.session_state.chips.bet_hero(bet)
        st.session_state.action = False
        st.rerun()
        villRaise = opponent_move.takeTurn(flop, turn, river, villain_hand)
    elif choice == "Fold":
        st.session_state.game_end = True
    elif choice[:4] == "Call":
        st.session_state.chips.call_hero()
        st.session_state.facing_bet = False
    elif choice == "Raise 3x":
        st.session_state.chips.raise_hero()
        st.session_state.facing_bet = False
        st.rerun()
        villRaise = opponent_move.takeTurn(flop, turn, river, villain_hand)
    
    if not villRaise:
        if st.session_state.river:
            st.session_state.game_end = True
        elif st.session_state.turn:
            st.session_state.river = True
        elif st.session_state.flop:
            st.session_state.turn = True
        else:
            st.session_state.flop = True



# Resets entire game to a new hand
reset = st.button("New Hand", type="primary")
if reset:
    st.session_state.deck = CardDeck()
    st.session_state.chips = Chips()
    st.session_state.flop = False
    st.session_state.turn = False
    st.session_state.river = False
    st.session_state.game_end = False
    st.session_state.facing_bet = False
    if random.random() < 0.5:
        st.session_state.btn = True # Hero on button
    else:
        st.session_state.btn = False # Villain on button
    st.session_state.action = not st.session_state.btn
    st.rerun()

import streamlit as st
from card_deck import CardDeck
import display_cards

#header
st.title("Poker 🃟 Bot.")
st.write(
    "Welcome to the minimalist Poker Bot. Designed by Elias Devadoss, Himal Pandey, and Marcus Lee."
)

#initializes the deck of cards, as well as the board and hands
if 'deck' not in st.session_state:
    st.session_state.deck = CardDeck()
flop = st.session_state.deck.get_flop()
turn = st.session_state.deck.get_turn()
river = st.session_state.deck.get_river()
hero_hand = st.session_state.deck.get_hero()
villain_hand = st.session_state.deck.get_villain()

#initializes the board to hidden
if 'flop' not in st.session_state:
    st.session_state.flop = False
if 'turn' not in st.session_state:
    st.session_state.turn = False
if 'river' not in st.session_state:
    st.session_state.river = False

#displays the hands and board
display_cards.display_players(hero_hand, villain_hand)
st.divider()
display_cards.display_board(flop, turn, river)

facing_bet = False
if(facing_bet==False):
    options = ["Check", "Bet 1/3 Pot", "Bet 2/3 Pot", "Bet 3/2 Pot"]
else:
    options = ["Fold", "Call", "Raise 3x"]
st.radio("Your action:", options, horizontal=True)

confirm = st.button("Confirm")
if confirm:
    st.session_state.flop = True
    st.rerun()

#resets entire game to a new hand
reset = st.button("New Hand", type="primary")
if reset:
    st.session_state.deck = CardDeck()
    st.session_state.flop = False
    st.session_state.turn = False
    st.session_state.river = False
    st.rerun()

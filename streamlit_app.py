import streamlit as st
from card_deck import CardDeck

st.title("Poker 🃟 Bot.")
st.write(
    "Welcome to the minimalist Poker Bot. Designed by Elias Devadoss, Himal Pandey, and Marcus Lee."
)

if 'deck' not in st.session_state:
    st.session_state.deck = CardDeck()
flop = st.session_state.deck.get_flop()
turn = st.session_state.deck.get_turn()
river = st.session_state.deck.get_river()
hero_hand = st.session_state.deck.get_hero()
villain_hand = st.session_state.deck.get_villain()

if 'flop' not in st.session_state:
    st.session_state.flop = False
if 'turn' not in st.session_state:
    st.session_state.turn = False
if 'river' not in st.session_state:
    st.session_state.river = False


st.subheader("Your Hand")
#possibly add opponent's hand
hero_col1, hero_col2, hero_col3 = st.columns([1, 1, 3], gap="medium", vertical_alignment="top")
with hero_col1:
    st.header(hero_hand[0], divider="violet")
with hero_col2:
    st.header(hero_hand[1], divider="violet")


col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="top")
with col1:
    st.subheader("Flop")
    if st.session_state.flop:
        st.header(flop[0], divider="violet")
    else:
        st.header("|⨔|", divider="violet")
with col2:
    st.subheader("")
    if st.session_state.flop:
        st.header(flop[1], divider="violet")
    else:
        st.header("|⨔|", divider="violet")
with col3:
    st.subheader("")
    if st.session_state.flop:
        st.header(flop[2], divider="violet")
    else:
        st.header("|⨔|", divider="violet")
with col4:
    st.subheader("Turn")
    if st.session_state.turn:
        st.header(turn[0], divider="violet")
    else:
        st.header("|⨔|", divider="violet")
with col5:
    st.subheader("River")
    if st.session_state.river:
        st.header(river[0], divider="violet")
    else:
        st.header("|⨔|", divider="violet")

facing_bet = False
if(facing_bet==False):
    options = ["Check", "Bet 1/3 Pot", "Bet 2/3 Pot", "Bet 3/2 Pot"]
else:
    options = ["Fold", "Call", "Raise 3x"]
st.radio("No Label", options, horizontal=True, label_visibility="hidden")

confirm = st.button("Confirm")
if confirm:
    st.session_state.flop = True
    st.rerun()


reset = st.button("New Hand", type="primary")
if reset:
    st.session_state.deck = CardDeck()
    st.session_state.flop = False
    st.session_state.turn = False
    st.session_state.river = False
    st.rerun()

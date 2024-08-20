import streamlit as st
from card_deck import CardDeck

st.title("Poker ♠️ Bot.")
st.write(
    "Welcome to the minimalist Poker Bot. Designed by Elias Devadoss, Himal Pandey, and Marcus Lee."
)

deck = CardDeck()
flop = deck.get_flop()
turn = deck.get_turn()
river = deck.get_river()
hero_hand = deck.get_hero()
villain_hand = deck.get_villain()


st.subheader("Your Hand")
hero_col1, hero_col2, hero_col3 = st.columns([1, 1, 3], gap="medium", vertical_alignment="top")
with hero_col1:
    st.header(hero_hand[0], divider="violet")
with hero_col2:
    st.header(hero_hand[1], divider="violet")


col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="top")
with col1:
    st.subheader("Flop")
    st.header(flop[0], divider="violet")
with col2:
    st.subheader("")
    st.header(flop[1], divider="violet")
with col3:
    st.subheader("")
    st.header(flop[2], divider="violet")
with col4:
    st.subheader("Turn")
    st.header(turn[0], divider="violet")
with col5:
    st.subheader("River")
    st.header(river[0], divider="violet")

options = ["", "", ""]
facing_bet = False
if(facing_bet==False):
    options = ["Check", "Bet x", "Bet y"]
else:
    options = ["Fold", "Call", "Raise 3x"]
st.radio("No Label", options, horizontal=True)


reset = st.button("New Hand", type="primary")
if reset:
    deck = CardDeck()

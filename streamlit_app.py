import streamlit as st
from card_deck import CardDeck

st.title("Poker ♠️ Bot")
st.write(
    "Welcome to the Poker Bot. Designed by Elias Devadoss, Himal Pandey, and Marcus Lee"
)

deck = CardDeck()
flop = deck.get_flop()
turn = deck.get_turn()
river = deck.get_river()
hero_hand = deck.get_hero()
villain_hand = deck.get_villain()

col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="top")

with col1:
    st.header("Flop")
    st.header(flop[0], divider="violet")

with col2:
    st.header("")
    st.header(flop[1], divider="violet")

with col3:
    st.header("")
    st.header(flop[2], divider="violet")

with col4:
    st.header("Turn")
    st.header(turn[0], divider="violet")

with col5:
    st.header("River")
    st.header(river[0], divider="violet")

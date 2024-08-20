import streamlit as st

st.title("Poker ♠️ Bot")
st.write(
    "Welcome to the Poker Bot. Designed by Elias Devadoss, Himal Pandey, and Marcus Lee"
)

col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="top")

with col1:
    st.header("Flop")
    st.header("9♠️", divider="violet")

with col2:
    st.header("")
    st.header("8♠️", divider="violet")

with col3:
    st.header("")
    st.header("7♠️", divider="violet")

with col4:
    st.header("Turn")
    st.header("6♠️", divider="violet")

with col5:
    st.header("River")
    st.header("5♠️", divider="violet")

import streamlit as st

st.title("Poker ♠️ Bot")
st.write(
    "Welcome to the Poker Bot. Designed by Elias Devadoss, Himal Pandey, and Marcus Lee"
)



col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="top")

with col1:
    st.header("Flop")
    st.header("9♠️")
    #st.text_area("No Label", value="9♠️", key=1, label_visibility="hidden")

with col2:
    st.header("")
    st.text_area("No Label", value="8♠️", key=2, label_visibility="hidden")

with col3:
    st.header("")
    st.text_area("No Label", value="7♠️", key=3, label_visibility="hidden")

with col4:
    st.header("Turn")
    st.text_area("No Label", value="6♠️", key=4, label_visibility="hidden")

with col5:
    st.header("River")
    st.text_area("No Label", value="5♠️", key=5, label_visibility="hidden")

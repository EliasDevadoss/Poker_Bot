import streamlit as st

def display_players(hero, villain):
    header_col1, header_col2 = st.columns([3,2], gap="medium", vertical_alignment="top")
    with header_col1:
        st.subheader("Your Hand")
    with header_col2:
        st.subheader("Opponent's Hand")
    play_col1, play_col2, play_col3, play_col4, play_col5 = st.columns(5, gap="medium", vertical_alignment="top")
    with play_col1:
        st.header(hero[0], divider="violet")
    with play_col2:
        st.header(hero[1], divider="violet")
    with play_col4:
        st.header("|⨔|", divider="violet")
    with play_col5:
        st.header("|⨔|", divider="violet")

def display_board(flop, turn, river):
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
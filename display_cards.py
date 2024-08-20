import streamlit as st

def display_hero(hero):
    st.subheader("Your Hand")
    hero_col1, hero_col2, hero_col3 = st.columns([1, 1, 3], gap="medium", vertical_alignment="top")
    with hero_col1:
        st.header(hero[0], divider="violet")
    with hero_col2:
        st.header(hero[1], divider="violet")
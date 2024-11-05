from pydantic import BaseModel
import os
import openai
import streamlit as st
import card_deck
import json

class ChosenAction(BaseModel):
    action: int

def callAI(flop, turn, river, villain_hand):
    # Retrieves the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')

    # Checks if the API key was retrieved successfully
    if api_key is None:
        st.error("API key not found! Make sure the environment variable is set correctly.")
    else:
        openai.api_key = api_key
    

    hand = villain_hand[0] + " " + villain_hand[1]
    turn_s = ""
    river_s = ""
    if st.session_state.flop:
        flop_s = "The flop is " + flop[0] + " " + flop[1] + " " + flop[2]
        if st.session_state.turn:
            turn_s =  ", the turn is " + turn[0]
            if st.session_state.river:
                river_s =  ", and the river is " + river[0]
    else:
        flop_s = "There are no cards out yet"
    if st.session_state.btn:
        position = "out of position"
    else:
        position = "in position"
    
    content = f"Your hand is {hand}. {flop_s}{turn_s}{river_s}. You are {position}. What do you do?"

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are poker player that plays GTO (Game Theory Optimal). You are playing heads up against one person and attempting to play overall according to GTO. This includes bluffing some percentage of the time. Cards will be passed in by a char for value and a char for suit, such that A♦️ is the ace of diamonds and T♠️ is the ten of spades. Respond only with an action in JSON format like: {\"action\": 0}. Use '0' for fold, '1' for check', '2' for call, '3' for bet, and '4' for raise."
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
        )

        # Extract the response content and parse it as JSON
        response_text = completion.choices[0].message['content'].strip()

        try:
            # Parse the response into a Python dictionary (assuming JSON format)
            response_json = json.loads(response_text)
            
            # Validate with the ChosenAction model
            chosen_action = ChosenAction(**response_json)
            st.write(f"Chosen bot action: {chosen_action.action}")

        except (ValueError, json.JSONDecodeError):
            st.error("Error: The response from OpenAI is not a valid JSON or integer.")

    except Exception as e:
        st.error(f"Error occurred: {e}")

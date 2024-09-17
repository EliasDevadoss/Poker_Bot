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
    flop = flop[0] + " " + flop[1] + " " + flop[2]
    turn = turn[0]
    river = river[0]
    position = "out of position"

    content = f"Your hand is {hand}. The flop is {flop}, the turn is {turn}, and the river is {river}. You are {position}. What do you do and why?"

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
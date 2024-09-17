from pydantic import BaseModel
import os
import openai
import streamlit as st

class ChosenAction(BaseModel):
    action: int

def callAI():
    # Retrieves the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')

    # Checks if the API key was retrieved successfully
    if api_key is None:
        st.error("API key not found! Make sure the environment variable is set correctly.")
    else:
        openai.api_key = api_key
    hand = "Js 9s"
    flop = "Jd Qs 3c"
    turn = "not out yet"
    river = "not out yet"
    position = "out of position"

    content = "Your hand is " + hand + ". The flop is " + flop + ",  the turn is " + turn + ", and the river is " + river + ". You are " + position +". What do you do and why?"

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are poker player that plays GTO (Game Theory Optimal). You are playing heads up against one person and attempting to play overall according to GTO. This includes bluffing some percentage of the time. Cards will be passed in by a char for value and a char for suit, such that A♦️ is the ace of diamonds and T♠️ is the ten of spades. Respond only with an int: '0' for fold, '1' for check', '2' for call, '3' for bet, and '4' for raise."
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
        )

        # Extract the response
        response_text = completion.choices[0].message['content']
        
        try:
            # Parse the response using the ChosenAction model
            chosen_action = ChosenAction(action=int(response_text.strip()))
        except ValueError:
            # Handle the case where the response cannot be converted to an integer
            st.write("Error: The response from OpenAI is not a valid integer.")

        # Display the action
        st.write(chosen_action.action)
    except Exception as e:
        st.error(f"Error occurred: {e}")
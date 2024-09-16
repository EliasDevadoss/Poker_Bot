from pydantic import BaseModel
import os
import openai
import streamlit as st
#from openai.error import InvalidRequestError, APIError

class ChosenAction(BaseModel):
    action: str

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

    #try:
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are poker player that plays GTO (Game Theory Optimal). You are playing heads up against one person and attempting to play overall according to GTO. This includes bluffing some percentage of the time. Cards will be passed in by a char for value and a char for suit, such that Ad is the ace of diamonds and Ts is the ten of spades. Respond with 'f' for fold, 'k' for check', 'c' for call, 'b' for bet, and 'r' for raise."
            },
            {
                "role": "user",
                "content": content
            }
        ],
        #response_format=ChosenAction,
    )

    # Extract the response
    response_text = completion.choices[0].message['content']
    
    # Parse the response using the ChosenAction model
    chosen_action = ChosenAction(action=response_text.strip())
    
    # Display the action
    st.write(chosen_action.action)

    bot_response = completion.choices[0].message
    if bot_response.parsed:
        st.write(bot_response.parsed)
    elif bot_response.refusal:
        st.write(bot_response.refusal)
    #except InvalidRequestError as e:
    #    st.write(f"Invalid request error: {e}")
    #except APIError as e:
    #    st.write(f"API error: {e}")
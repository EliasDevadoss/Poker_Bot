from pydantic import BaseModel
#from openai.error import InvalidRequestError, APIError

class ChosenAction(BaseModel):
    action: str

def callAI():
    hand = "Js 9s"
    flop = "Jd Qs 3c"
    turn = "not out yet"
    river = "not out yet"
    position = "out of position"

    content = "Your hand is " + hand + ". The flop is " + flop + ",  the turn is " + turn + ", and the river is " + river + ". You are " + position +". What do you do and why?"

    #try:
    completion = openai.beta.chat.completions.parse(
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
        response_format=ChosenAction,
    )

    bot_response = completion.choices[0].message
    if bot_response.parsed:
        st.write(bot_response.parsed)
    elif bot_response.refusal:
        st.write(bot_response.refusal)
    #except InvalidRequestError as e:
    #    st.write(f"Invalid request error: {e}")
    #except APIError as e:
    #    st.write(f"API error: {e}")
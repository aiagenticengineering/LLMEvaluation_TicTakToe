ticktaktoe# %%
import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI
client = OpenAI()

# %%
def player_o(board):

    response = client.responses.create(
        model="gpt-5",
        instructions="""
        You are Player O in a Tic-Tac-Toe game.
        Play defensively.
        First prevent X from winning, then try to win.
        Return only the position you want to play.
        """,
        input=f"""
        Current board:

        {board}

        Choose your move.
        """
    )
    

    return response.output_text

# %%
def player_x(board):

    response = client.responses.create(
        model="gpt-5",
        instructions="""
        You are Player X in a Tic-Tac-Toe game.
        Play defensively.
        First prevent O from winning, then try to win.
        Return only the position you want to play.
        """,
        input=f"""
        Current board:

        {board}

        Choose your move.
        """
    )
    

    return response.output_text

# %%
board = """
X | O | X
---------
O | O | X
---------
X |   |
"""
print(player_x(board))

# %%
board = """
X | O | X
---------
O | O | X
---------
X |   |
"""
print(player_o(board))



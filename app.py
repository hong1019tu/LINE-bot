import os
import sys


from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from fsm import TocMachine
from utils import send_text_message
from transitions import Machine

# import pygraphviz
from transitions.extensions import GraphMachine


load_dotenv()


machine = TocMachine(
    states=["highlights","showpic","initial","game_info", "stats_leader_info", "teams_info" , "rank_info","player_info","point_leader","assist_leader","rebound_leader","kings","braves","dreamers","pilots","steelers","lioneers","choose_player","choose_pic"],
    transitions=[
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "highlights",
            "conditions": "is_going_to_highlights",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "game_info",
            "conditions": "is_going_to_game_info",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "stats_leader_info",
            "conditions": "is_going_to_statsleaderinfo",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "teams_info",
            "conditions": "is_going_to_teams_info",
        },
        {
            "trigger": "advance",
            "source": "teams_info",
            "dest": "kings",
            "conditions": "is_going_to_kings",
        },
        {
            "trigger": "advance",
            "source": "teams_info",
            "dest": "braves",
            "conditions": "is_going_to_braves",
        },
        {
            "trigger": "advance",
            "source": "teams_info",
            "dest": "pilots",
            "conditions": "is_going_to_pilots",
        },
        {
            "trigger": "advance",
            "source": "teams_info",
            "dest": "dreamers",
            "conditions": "is_going_to_dreamers",
        },
        {
            "trigger": "advance",
            "source": "teams_info",
            "dest": "lioneers",
            "conditions": "is_going_to_lioneers",
        },
        {
            "trigger": "advance",
            "source": "teams_info",
            "dest": "steelers",
            "conditions": "is_going_to_steelers",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "rank_info",
            "conditions": "is_going_to_rank_info",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "choose_player",
            "conditions": "is_going_to_choose_player",
        },
        {
            "trigger": "advance",
            "source": "choose_player",
            "dest": "player_info",
            "conditions": "is_going_to_player_info",
        },
        {
            "trigger": "advance",
            "source": "choose_pic",
            "dest": "showpic",
            "conditions": "is_going_to_showpic",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "choose_pic",
            "conditions": "is_going_to_choose_pic",
        },
        {
            "trigger": "advance",
            "source": "stats_leader_info",
            "dest": "point_leader",
            "conditions": "is_going_to_point_leader",
        },
        {
            "trigger": "go_back_leader",
            "source": ["point_leader","rebound_leader","assist_leader"],
            "dest": "stats_leader_info",

        },
        {
            "trigger": "go_back_team",
            "source": ["kings", "lioneers","braves","pilots","dreamers","steelers"],
            "dest": "teams_info",

        },
        {
            "trigger": "advance",
            "source": "stats_leader_info",
            "dest": "assist_leader",
            "conditions": "is_going_to_assist_leader",
        },
        {
            "trigger": "advance",
            "source": "stats_leader_info",
            "dest": "rebound_leader",
            "conditions": "is_going_to_rebound_leader",
        },
        {   
            "trigger": "advance", 
            "source": ["highlights","showpic","stats_leader_info","teams_info","rank_info","choose_pic","choose_player","game_info","highlights"], 
            "dest": "initial",
            "conditions": "back_to_menu",
        },
        {   
            "trigger": "go_back_player", 
            "source": "player_info", 
            "dest": "choose_player",
        },
        {   
            "trigger": "advance", 
            "source": "showpic", 
            "dest": "choose_pic",
            "conditions": "back_to_choose_pic",
        },
    ],
    initial="initial",
    auto_transitions=False,
    show_conditions=True,
)




app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "invalid input !please try again\n\n********************************\nwhen you in menu:\nshow game information\nshow team picture\nshow player information\nshow rank information\nshow stats leader\nshow highlights\nshow team information\n********************************\nwhen you in stats leader:\npoint\nrebound\nassist\n********************************\nwhen you in player information:\nenter player name\n********************************\nwhen you in team information:\nkings\nbraves\npilots\nlioneers\ndreamers\nsteelers\n********************************\nwhen you in team picture:\nafter pressing the button,enter one more time for a new button\n********************************\nin any state:\nenter back to menu to back to menu")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)

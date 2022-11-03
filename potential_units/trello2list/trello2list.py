from pathlib import Path
from typing import *
import json
from dataclasses import dataclass, fields

import requests

BoardID = NewType("BoardID", str)
JSON = NewType("JSON", str)

TrelloJSONService = NewType("TrelloJSONService", Callable[[BoardID], JSON])

def get_json_from_examples(board_id: BoardID) -> JSON:
    example_dir = Path(__file__).parent.parent / "examples"
    board_path = example_dir / (board_id + ".json")
    text: JSON = board_path.read_text()
    if json.loads(text):
        return text


def get_json_from_trello(board_id: BoardID) -> JSON:  # TODO: Get API Key and send with request
    trello_url_formatter = "https://trello.com/b/{board_id}.json"
    url = trello_url_formatter.format(board_id=board_id)
    r = requests.get(url=url)
    text = r.text
    if json.loads(text):
        return text



# board_id: BoardID = "7jkTcy2a"  Needs API key,
# text = get_json_from_trello(board_id)
# print(text)

board_id: BoardID = "dja23n2"
text = get_json_from_examples(board_id)
text



print(text)

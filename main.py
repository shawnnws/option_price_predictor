# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import flask
from flask import Flask
from typing import Dict, Any
from flask import request
import json
from pydantic import BaseModel

# to check version of dependencies, do pip freeze | grep <library>

print(f"__name__: {__name__}")  # __name__ = "__main__", or "C:\Users\Shawn\Desktop\python_notes\option_price_predictor/main.py"
flask_app: Flask = Flask(__name__)  # C:\Users\Shawn\Desktop\python_notes\option_price_predictor/templates/img.png

class StockInput(BaseModel):
    stock: str

# when we send data over from server to client, and client to server, its in strings / bytes format
# we serialize (convert data class / python data structures into a raw string / bytes format) it before sending
# data_sent_over: str = """{
#     "stock": 100
# }"""

# when we handle data on server / client in python, we typically handle it as a Dictionary, or a Data Class
# loaded_dictionary: Dict[str, float] = {
#     "stock": 100
# }

# REST -> Protocol (set of rules that applications follow to send and receive data)
@flask_app.route("/call_option_price", methods=["GET"])
def call_option_price() -> Dict[str, Any]:
    # get input data from the request "data" field
    body: bytes = request.data

    print(body, type(body))

    # To convert raw_data (bytes / JSON string) back into a dictionary, use json.loads(raw_data)
    # we deserialize the raw data / convert the raw byte data into a dictionary, so that its easier to handle it in python
    # I.E, its easier to get a value by key from a dictionary, vs scanning the bytes / string
    body_dict: Dict[str, Any] = json.loads(body)
    stock_input: StockInput = StockInput.parse_obj(body_dict)

    # JSON -> Javascript Object Notation (JSON), actually is a misnomer (string, key value pairs)
    return {
        "stock": stock_input.stock,
        "price": 100
    }

if __name__ == "__main__":
    flask_app.run(port=6000)    #   GET http://localhost:6000/shawn_route     # http://127.0.0.1:6000/shawn_route


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import flask
from flask import Flask
from typing import Dict, Any

print(f"__name__: {__name__}")  # __name__ = "__main__", or "C:\Users\Shawn\Desktop\python_notes\option_price_predictor/main.py"
flask_app: Flask = Flask(__name__)  # C:\Users\Shawn\Desktop\python_notes\option_price_predictor/templates/img.png


@flask_app.route("/shawn_route", methods=["GET"])
def call_option_price() -> Dict[str, Any]:
    return {
        "AAPL": 100
    }

if __name__ == "__main__":
    flask_app.run(port=6000)    #   GET http://localhost:6000/shawn_route     # http://127.0.0.1:6000/shawn_route


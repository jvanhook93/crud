from flask import (
  Flask,
  request
)

app = Flask(__name__)

from app.database import data_types


@app.get("/")
def index():
  out = data_types.scan()
  return out


# @app.get("/integers")
# def integers():
#   out = data_type.select_by_type(name="Integer")
#   return out


# @app.get("/floats")
# def floats():
#   out = data_type.select_by_type(name="Float")
#   return out


# @app.get("booleans")
# def bools():
#   out = data_type.select_by_type(name="Boolean")
#   return out

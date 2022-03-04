from flask import Flask, render_template
app = Flask('app')
from game import *

@app.route('/')
def hello_world():
  return render_template("index.html",name = game_return(),img=img(), data=get_data(), length=len(get_data()))

app.run(host='0.0.0.0', port=8080)

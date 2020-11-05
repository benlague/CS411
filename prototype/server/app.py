from flask import Flask
import yaml
import os

app = Flask(__name__)
creds = yaml.safe_load(open("creds.yaml", "r"))

@app.route("/")
def index(): 
    return "Hello World"



if __name__ == "__main__":
    app.run(port=4000, debug=True)
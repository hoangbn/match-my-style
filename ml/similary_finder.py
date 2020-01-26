from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def get_most_similar():
    cont = request.json
    for url in cont:
        pass
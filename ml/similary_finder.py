from flask import Flask, request, jsonify

app = Flask(__name__)

user_data = {
                "shirts": [], 
                "pants": []
            }
cata_data = {
                "shirts": [], 
                "pants": []
            }

def 

@app.route("/getSimilar")
def get_most_similar():
    threshold = request.args.get("percentage")



if __name__ == '__main__':
    
    app.run()
import uuid
import datetime
from http import HTTPStatus
from google.cloud.firestore_v1.client import Client

from firebase_admin import credentials, initialize_app, firestore, storage
from flask import Flask, request, jsonify

from utils import valid_input
from similary_finder import purge_products, get_most_similar

app = Flask(__name__)

cred = credentials.Certificate("secret.json")
initialize_app(cred, {
    "storageBucket": "match-my-style.appspot.com"
})

# Put everything in 1 file for now (no time)
USERS = "users"
db: Client = firestore.client()
bucket = storage.bucket()


@app.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    header["Access-Control-Allow-Headers"] = "*"
    return response


def upload_file(file, cloud_path):
    image_blob = bucket.blob(cloud_path)
    image_blob.upload_from_file(file_obj=file, content_type=file.content_type)
    return image_blob.generate_signed_url(datetime.timedelta(days=365))


def add_item(username, item_type, file):
    doc_ref = db.collection(USERS).document(username)
    doc = doc_ref.get().to_dict()
    if doc_ref.get().to_dict() is None:
        return jsonify("use do"
                       "es not exist"), HTTPStatus.NOT_FOUND
    image_link = upload_file(file, f"{USERS}/{username}/{item_type}/{str(uuid.uuid4())}.jpg")
    doc[item_type].append(image_link)
    doc_ref.update(doc)
    return jsonify(image_link)


@app.route('/users', methods=['POST'])
def create_user():
    user_info = request.get_json()
    if not valid_input(user_info, ["username"]):
        return jsonify("invalid request body"), HTTPStatus.BAD_REQUEST
    username = user_info.get("username")
    doc_ref = db.collection(USERS).document(username)
    doc = doc_ref.get().to_dict()
    if doc is not None:
        return jsonify("username exists"), HTTPStatus.CONFLICT
    doc = {"pants": [], "shirts": []}
    doc_ref.set(doc)
    return jsonify("user created")


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    doc_ref = db.collection(USERS).document(username)
    doc = doc_ref.get().to_dict()
    if doc is None:
        return jsonify("username not found"), HTTPStatus.NOT_FOUND
    return jsonify(doc)


@app.route('/users/<username>/pants', methods=['POST'])
def add_pants(username):
    if "file" not in request.files:
        return jsonify("file missing in the header"), HTTPStatus.BAD_REQUEST
    return add_item(username, "pants", request.files["file"])


@app.route('/users/<username>/shirts', methods=['POST'])
def add_shirts(username):
    if "file" not in request.files:
        return jsonify("file missing in the header"), HTTPStatus.BAD_REQUEST
    return add_item(username, "shirts", request.files["file"])


@app.route('/users/<username>/getSimilarityScore/<threshold>', methods=['GET'])
def get_similar(username, threshold):
    doc_ref = db.collection(USERS).document(username)
    doc = doc_ref.get().to_dict()
    if doc is None:
        return jsonify("username not found"), HTTPStatus.NOT_FOUND
    return get_most_similar(threshold, doc.get("shirts"), doc.get("pants"))


@app.route("/purge_products_ml")
def purge_products_ml():
    purge_products()
    return jsonify("purged")

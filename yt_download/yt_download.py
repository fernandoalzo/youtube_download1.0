from flask import Blueprint

yt_download = Blueprint("yt_download", __name__, template_folder='templates')

@yt_download.route("/")
def home():
    return "hello world"

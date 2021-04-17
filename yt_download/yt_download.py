from flask import Blueprint, render_template

yt_download = Blueprint("yt_download", __name__, template_folder='templates')

@yt_download.route("/")
@yt_download.route("/home")
def home():
    return render_template("home.html")

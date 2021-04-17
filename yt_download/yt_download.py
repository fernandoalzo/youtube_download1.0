from flask import Blueprint, render_template

yt_download = Blueprint("yt_download", __name__, template_folder='templates')

@yt_download.route("/")
def home():
    return render_template("home.html")

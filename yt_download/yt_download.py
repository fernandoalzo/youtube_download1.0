from flask import Blueprint, render_template, url_for
from .formulario import formulario_link_video

yt_download = Blueprint("yt_download", __name__, template_folder='templates')

@yt_download.route("/", methods=['GET', 'POST'])
@yt_download.route("/home", methods=['GET', 'POST'])
@yt_download.route("/descargar", methods=['GET', 'POST'])
def descargar():
    formulario = formulario_link_video()
    link_video = formulario.link_video.data

    if formulario.validate_on_submit():
        print("Link del video: ")
        print(link_video)

    return render_template("home.html", formulario = formulario)
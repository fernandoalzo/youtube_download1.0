from flask import Blueprint, render_template, url_for, send_file, redirect
from .formulario import formulario_link_video
from .funciones import funciones

yt_download = Blueprint("yt_download", __name__, template_folder='templates')

@yt_download.route("/", methods=['GET', 'POST'])
@yt_download.route("/home", methods=['GET', 'POST'])
@yt_download.route("/descargar", methods=['GET', 'POST'])
def descargar():
    formulario = formulario_link_video()
    link_video = formulario.link_video.data

    if formulario.validate_on_submit():
        download_video = funciones.download_vidoes_as_mp3(link_video)
        if download_video == 0:
            funciones.comprimir("./temp")
            funciones.eliminar_archivos_usados("./temp")
            funciones.mover_archivos("./canciones.zip")
            return redirect(url_for('yt_download.descargar_comprimido'))

        else:
            print("==================================")
            print("Ocurrio un error!!!")
            print("==================================")

    return render_template("home.html", formulario=formulario)

@yt_download.route("/descargar_comprimido")
def descargar_comprimido():
    zip_file = "./temp/canciones.zip"
    return send_file(zip_file, as_attachment=True)
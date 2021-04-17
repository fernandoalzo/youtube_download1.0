from flask import Flask, render_template
from yt_download.yt_download import yt_download

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

app.register_blueprint(yt_download)

if __name__=="__main__":
    app.run()
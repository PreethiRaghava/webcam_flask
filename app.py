import os
import urllib.request
from flask import Flask, render_template
from werkzeug.utils import secure_filename
from flask import Flask
from flask_cors import CORS
# app = Flask('flaskwp1')
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

cwd = os.getcwd()
print(cwd)

template_dir = os.path.dirname(os.path.dirname(
    os.path.abspath(os.path.dirname(__file__))))
# template_dir = os.path.join(template_dir, 'frontend')
template_dir = os.path.join(cwd, 'static')
print(template_dir)

app = Flask(__name__, template_folder=template_dir)


@app.route("/", methods=['GET','POST'])
def hello():
    return render_template('basic.html')


if __name__ == "__main__":
    app.run(host='10.5.11.152',debug=True, port = 5000)

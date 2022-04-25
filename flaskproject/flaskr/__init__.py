import os
from getTableData import readTable
from flask import Flask, Blueprint

api_bp = Blueprint("api", __name__)
app = Flask(__name__, instance_relative_config=True)

def readIndexFile():
    with open("index.html", "r") as file:
        return file.read()
contents = readIndexFile()

@api_bp.route('/books')
def website():
    result=readTable()
    content=""
    for item in result:
        content=content+"<h5>"+item["title"]+"</h5>"
        content=content+"<div>"+item["author"]+"</div>"
        content=content+"<div>"+item["place"]+": "+item["publisher"]+"</div>"
        content=content+"<div>"+item["year"]+", "+item["edition"]+", "+item["pages"]+"</div>"
        content=content+"<div>"+item["isbn"]+"</div>"
        content=content+"<div>"+item["ddc"]+"; "+item["keywords"]+"</div>"
        content=content+'<a href="'+item["table_url"]+'">'+item["table_url"]+", "+"</a>"
        content=content+'<a href="'+item["summary_url"]+'">'+item["summary_url"]+"</a>"
    return contents.replace("$placeholder", content)

def create_app(test_config=None):
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_bp)
    return app
create_app()
app.run(host="0.0.0.0", port=80)
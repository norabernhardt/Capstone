import json
import os

from flaskr.getTableData import readTable

tablename="table-for-preferences"

from flask import Flask, Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route('/books')
def table():
    result=readTable()
    return json.dumps(result)
doctype='<!DOCTYPE html><html lang="en"><head><link rel="stylesheet"href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css"/><meta charset="UTF-8"><title>Title</title></head><body><p>Hello from Noris Webserver</p>$placeholder</body></html>'
@api_bp.route('/bookshtml')
def html():
    result=readTable()
    content=""
    for item in result:
        print(item)
        content=content+"<h4>"+item["title"]+"</h4>"
        content=content+"<p>"+item["author"]+"</p>"
        content=content+"<p>"+item["place"]+": "+item["publisher"]+"</p>"
        content=content+"<p>"+item["year"]+", "+item["edition"]+", "+item["pages"]+"</p>"
        content=content+"<p>"+item["isbn"]+"</p>"
        content=content+"<p>"+item["ddc"]+"; "+item["keywords"]+"</p>"
        content=content+"<a href>"+item["table_url"]+", "+item["summary_url"]+"</a>"
        #url nicht richtig hinterlegt
        content=content+"<a href>"+item["summary_url"]+"</a>"
    return doctype.replace("$placeholder",content)


# @api_bp.route('/table/<tablename>')
# def table(tablename):
#     return json.dumps(tablename)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_bp)

    return app
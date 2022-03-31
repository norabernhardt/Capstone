import json
import os
from flask import Flask, Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route('/s3/<bucketname>')
def buckets(bucketname):
    #s3_data=get_s3_data. functionname (bucketname)
    return json.dumps([{"name": "bucketname"}])

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
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
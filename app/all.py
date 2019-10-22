
from flask import Blueprint
import os
from .tasks import make_file
bp = Blueprint("all", __name__)
from app.models.testpython import TestPython


@bp.route("/")
def index():
    return "Hello!"

@bp.route("/<string:fname>/<string:content>")
def makefile(fname, content):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    make_file.delay(fpath, content)
    return f"Find your file @ <code>{fpath}</code>"

@bp.route('/finished')
def get_finished_data():
    try:
        finished_data = TestPython.query.all()
        result = []
        for data in finished_data:
            result.append({
                'id':data.id,
                'sum':data.sum,
                'start':data.start,
                'end':data.end,
                'iterations':data.iterations,
            })
        _result = {}
        _result['result'] = result
        return _result,200
        
    except error:
        print(error)
        pass
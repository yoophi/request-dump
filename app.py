from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/dump', methods=['GET', 'POST'])
def dump_request():
    args = dict(request.args)
    data = request.data.decode('utf-8')
    form = dict(request.form)
    json = request.get_json()
    headers = dict(request.headers)
    env = {
        k: str(request.environ.get(k))
        for k in request.environ.keys()
    }

    resp = {'args': args, 'data': data, 'form': form, 'json': json, 'headers': headers, 'request.env': env}

    return jsonify(resp)

from flask import Flask


app = Flask(__name__)


@app.route('/application_1')
def index():
    return '<h1>Micro Service 1</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)

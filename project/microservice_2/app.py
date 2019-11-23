from flask import Flask


app = Flask(__name__)


@app.route('/application_2')
def index():
    return '<h1>Micro Service 2</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)

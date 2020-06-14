from flask import Flask, render_template

app = Flask(__name__, static_folder='../templates/dist/static', template_folder='../template/dist')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

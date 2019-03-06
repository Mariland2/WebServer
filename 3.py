from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Привет, яндекс! Я - Кирилл</h1>"

@app.route('/image_sample')
def image_sample():
        return '''<img src="{}" alt="здесь должна была быть картинка, 
        но не нашлась">'''.format(url_for('static', filename='img/1.jpeg'))



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
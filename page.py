from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello1():
    return render_template('home1.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/guestbook')
def guestbook():
    return render_template('guestbook.html')

@app.route('/picture')
def picture():
    return render_template('picture.html')

if __name__ == '__main__':
    app.run(debug=True)
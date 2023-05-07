from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')
7799331117
@app.route('/goodbye/<name>')
def goodbye(name):
    return render_template('house.html',name=name)

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html',post_id=post_id)

if __name__ == '__main__':
    app.run(debug=True)
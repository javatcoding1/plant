from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the 'flexbox2.html' page
@app.route('/')
def flexbox2():
    return render_template('welcomepage.html')
@app.route('/flexbox2')
def flexbox1():
    return render_template('flexbox2.html')
@app.route('/index')
def upload():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

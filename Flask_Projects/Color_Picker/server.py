from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html', color='white')

@app.route('/submit', methods=['POST'])
def color():
	color = "rgb("+ request.form['red'] +", "+request.form['blue']+", "+request.form['green']+")"
	return render_template('index.html', color=color)

app.run(debug=True)
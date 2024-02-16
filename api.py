from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Helllo World !"

app.run(debug=True)

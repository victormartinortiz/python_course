from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, software engineer graduated from Platzi!'


if __name__ == "__main___":
	app.run()
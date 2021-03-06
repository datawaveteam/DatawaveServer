import os
from flask import Flask, request, jsonify
import requests
import bleach

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello There, from DataWave.'

@app.route('/stream')
def stream():
	url = request.args.get('url')
	r = requests.get(url)
	attrs = {'*': ['style']}
	tags = ['p', 'em', 'strong', 'script', 'style', 'link']
	styles = ['color', 'font-weight']
	result = bleach.clean( r.text, attrs, tags, styles)
	sanitized_result = {'data':{'url':url, 'body': [result]}}
	return jsonify(sanitized_result)

if __name__ == '__main__':
	app.run(debug=True)
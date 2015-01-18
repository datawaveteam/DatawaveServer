from flask import Flask
import requests
import bleach

app = Flask(__name__)

@app.route('/')
def hello():
	r = requests.get('http://en.wikipedia.org/wiki/HTTP_message_body')
	attrs = {'*': ['style']}
	tags = ['p', 'em', 'strong', 'script', 'style', 'link']
	styles = ['color', 'font-weight']
	sanitized_result = bleach.clean( r.text, attrs, tags, styles)
	return sanitized_result


if __name__ == '__main__':
    app.run()
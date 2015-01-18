from flask import Flask, request
from BeautifulSoup import BeautifulSoup as Soup
import wikipedia, string

app = Flask(__name__)

@app.route('/<query>')
def index(query):
	try:
		text = wikipedia.summary(query)
	except Exception as e:
		text = "DisambiguationError: Be more specific and please try again."
	allowed_chars = string.letters + string.digits + " .?!" # 66 chars total
	filtered_summary = ''.join( char for char in text if  char in allowed_chars )
	jsonify = """{ "summary" : \"""" + filtered_summary + "\" }"
	return jsonify


if __name__ == '__main__':
    app.run(host="0.0.0.0")

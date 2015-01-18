from flask import Flask, request, jsonify
from BeautifulSoup import BeautifulSoup as Soup
import wikipedia, string
import requests
import bleach

app = Flask(__name__)

@app.route('/stream') # Moved here because of naming convention. 
def stream():
	try:
		url = request.args.get('url')
		r = requests.get(url)
	except Exception as e:
		url = 'Invalid Url'
		r = {'text': 'Invalid request'}

	html_doc = r.text
	soup = Soup(html_doc)

	# The below portion utilizes Bleach to clean up the html.
	attrs = {'*': ['style']}
	tags = ['p', 'em', 'strong', 'script', 'style', 'link']
	styles = ['color', 'font-weight']
	result = bleach.clean( html_doc, attrs, tags, styles)
	# End of bleaching

	sanitized_result = {'summary': [result]}
	return jsonify(sanitized_result)

@app.route('/<query>')
def index(query):
	try:
		text = wikipedia.summary(query)
	except Exception as e:
		text = "DisambiguationError: Be more specific and please try again."
	allowed_chars = string.letters + string.digits + " .?!" # 66 chars total
	filtered_summary = ''.join( char for char in text if  char in allowed_chars )
	result = """{ "summary" : \"""" + filtered_summary + "\" }"
	# Utilizing the jsonify module from flask. 
	return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

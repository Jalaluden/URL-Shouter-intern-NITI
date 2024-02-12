from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return render_template('index.html', short_url=request.url_root + short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_mapping:
        return redirect(url_mapping[short_url])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)

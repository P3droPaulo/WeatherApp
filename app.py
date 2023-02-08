from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    city = 'Belo Horizonte'
    return render_template('homepage.html', city=city)

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
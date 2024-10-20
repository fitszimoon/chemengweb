from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/joker')
def joker_info():
    return render_template('joker.html')

@app.route('/morgana')
def morgana_info():
    return render_template('morgana.html')

if __name__ == '__main__':
    app.run(debug=True)

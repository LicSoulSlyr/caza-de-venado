from flask import Flask, render_template

app = Flask(__name__)

@app.route('/informe cientifico')
def home():
    return render_template('informe.html')

if __name__ == '__main__':
    app.run(debug=True)
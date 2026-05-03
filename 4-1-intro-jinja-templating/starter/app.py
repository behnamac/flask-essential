from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user={'username':'Behnam'}
    return render_template('index.html',title='home',user=user)

if __name__ == '__main__':
    app.run(debug=True)

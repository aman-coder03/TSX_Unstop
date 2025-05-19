
from flask import Flask, render_template
from data import projects

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project_page():
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)

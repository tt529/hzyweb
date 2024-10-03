from os import path
from pathlib import Path
from flask import Flask, render_template
from flask_frozen import Freezer

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/<page>.html')
def pages(page):
    return render_template(f'pages/{page.lower()}.html')

@freezer.register_generator
def page_generator():
    yield '/'
    pages = ['about']  # 添加你所有的页面名称
    for page in pages:
        yield f'/{page}.html'

if __name__ == "__main__":
    app.run(port=8080)


    # .\venv\Scripts\activate
    # deactivate  

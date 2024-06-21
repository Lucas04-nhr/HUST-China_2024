from os import path

import pypandoc
from flask import Flask, render_template
from flask_frozen import Freezer

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
# app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)


@app.cli.command()
def freeze():
    freezer.freeze()


@app.cli.command()
def serve():
    freezer.run()


@app.route('/')
def home():
    md_content = pypandoc.convert_file('docs/home.md', 'html')
    return render_template('base.html',
                           title='Home',
                           md_content=md_content)


@app.route('/<page>')
def pages(page):
    md_content = pypandoc.convert_file(f'docs/{page.lower()}.md', 'html')
    return render_template('base.html',
                           title=page.title().replace('-', ' '),
                           md_content=md_content)


# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)

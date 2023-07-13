"""
This will convert text that the user will send from the HTML website to the Python endpoint.
"""
from deep_translator import GoogleTranslator
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')


def translate_he(text: str):
    """
    Translate text to Hebrew.
    :param text: The text to translate.
    :return: The translated text or None if the length of the text is not between 0 and 300.
    """
    if 0 < len(text) > 300:
        return None
    return GoogleTranslator(source='auto', target='iw').translate(text)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the index page and handle POST requests.
    :return: The rendered index template or the translated text.
    """
    if request.method == 'POST':
        res = request.form.get('text')
        return render_template('index.html', res=translate_he(res))
    return render_template('index.html')


app.run(debug=False)

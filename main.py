from flask import Flask, request, render_template
from deep_translator import GoogleTranslator


app = Flask(__name__, template_folder='.')

LIMAT_CHAR = 300

def translate_he(text):
    if not text or len(text) > LIMAT_CHAR:
        return
    return GoogleTranslator(source='auto', target='iw').translate(text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        res = request.form.get('text')
        return render_template('index.html', res=translate_he(res))
    return render_template('index.html')

app.run(debug=True)



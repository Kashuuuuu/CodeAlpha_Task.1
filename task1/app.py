from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['language']
        translated = translator.translate(text_to_translate, dest=target_language)
        return render_template('index.html', original=text_to_translate, translated=translated.text, target_language=LANGUAGES[target_language], LANGUAGES=LANGUAGES)
    return render_template('index.html', original=None, translated=None, LANGUAGES=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)

# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_html = request.form.get("button_html")
    button_disc = request.form.get("button_disc")
    button_db = request.form.get("button_db")
    email = request.form.get("email")
    text = request.form.get("text")
    if text:
        with open("aram.txt","a") as feedback:
            feedback.write(email)
            feedback.write("\n")
            feedback.write(text)
            feedback.write("\n")
            feedback.write("----------------\n")
    return render_template('index.html', button_python=button_python, button_html=button_html, button_disc=button_disc, button_db=button_db)

    


if __name__ == "__main__":
    app.run(debug=True)

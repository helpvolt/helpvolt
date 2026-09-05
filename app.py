from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Agora ele vai procurar um arquivo chamado index.html na pasta templates
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
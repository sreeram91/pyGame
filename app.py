from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    choice = request.form.get("choice")
    result = None
    if choice == "rock":
        result = "tie"
    elif choice == "paper":
        result = "you win"
    else:
        result = "you lose"
    return render_template("play.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' ,port=3002)

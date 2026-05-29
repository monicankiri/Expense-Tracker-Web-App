from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        
        try:
            amount = int(request.form.get("amount"))
        except:
            amount = 0

        expenses.append({"name": name, "amount": amount})

    total = sum(exp["amount"] for exp in expenses)

    return render_template("index.html", expenses=expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)
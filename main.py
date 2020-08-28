from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="./templates", static_url_path="/templates")
app.debug=True

username = "bob"
currentBudget = 350.0


@app.route("/")
def homePage():

    print("User connected to the homepage")


    return render_template("homepage.html", user= username, budget=currentBudget)


@app.route("/budget", methods=["GET", "POST"])
def changeBudget():
    if request.method == "POST":
        global currentBudget
        newBudget = request.form.get("new_budget")
        print(newBudget)
        currentBudget = newBudget
        return jsonify({"new_budget":newBudget})

    return render_template("budget.html", user= username, budget=currentBudget)


if __name__ == "__main__":
    app.run()

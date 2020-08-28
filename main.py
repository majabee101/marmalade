from flask import Flask, render_template, request, jsonify


app = Flask(__name__, static_folder="./templates", static_url_path="/templates")
app.debug=True

username = "Samj"
currentBudget = 350


@app.route("/")
def mainPage():

    print("User connected to the mainpage")


    return render_template("mainpage.html", user= username, budget=currentBudget)

@app.route("/homepage", methods=["GET", "POST"])
def homePage():

    print("user connected to homepage")

    return render_template("homepage.html")


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

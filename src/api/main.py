from flask import Flask, render_template, request, jsonify
import http.client


app = Flask(__name__, static_folder="../templates", static_url_path="/templates")
app.debug=True

username = "Samj"
currentBudget = 350


@app.route("/")
def mainPage():

    print("User connected to the mainpage")


    return render_template("mainpage.html", user= username, budget=getBudget(1))

@app.route("/homepage", methods=["GET", "POST"])
def homePage():

    print("User connected to the homepage")

    return render_template("homepage.html",user= username, budget=getBudget(1))


@app.route("/foodpage", methods=["GET", "POST"])
def foodPage():

    print("User connected to the foodpage")

    return render_template("foodpage.html")

@app.route("/analytics", methods=["GET", "POST"])
def Analytics():

    print("User connected to the foodpage")

    return render_template("analytics.html")

@app.route("/map", methods=["GET", "POST"])
def Map():

    print("User connected to the map")

    return render_template("map.html")


@app.route("/recipes", methods=["GET", "POST"])
def Recipes():

    print("User connected to the recipe page")

    return render_template("recipes.html")


@app.route("/vouchers", methods=["GET", "POST"])
def Vouchers():

    print("User connected to the voucher page")

    return render_template("vouchers.html")

@app.route("/budget", methods=["GET", "POST"])
def changeBudget():
    if request.method == "POST":
        newBudget = request.form.get("new_budget")
        print(newBudget)
        updateBudget(1, newBudget)
        return jsonify({"new_budget":newBudget})

    return render_template("budget.html", user= username, budget=currentBudget)



# get budget based on user id

def getBudget(id):
    baseurl = "smartfoods1.azurewebsites.net"
    url = "/api/GetBudget?UserId=" + str(id)

    conn = http.client.HTTPSConnection(baseurl)
    conn.request("GET", url)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()
    return data1.decode('utf-8')

# update budget based on user id

def updateBudget(id, newVal):
    baseurl = "smartfoods1.azurewebsites.net"
    url="/api/SetBudget?UserId={}&Budget={}".format(id,newVal)

    conn = http.client.HTTPSConnection(baseurl)
    conn.request("GET", url)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()
    print(data1.decode('utf-8'))

    return None


if __name__ == "__main__":
    app.run()

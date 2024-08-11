from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        passagain = request.form.get("passagain")
        nameCharCount = len(name)
        remain = 8 - nameCharCount
        if nameCharCount <= 7:
            return render_template("countError.html", name=name, remain=remain)
        if password != passagain:
            return render_template("error.html", name=name)
        if "@" not in email:
            return render_template("emailerror.html", name=name)
        else:
            return render_template("login.html", name=name)
    else:
        #hakerobebiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
        print(f"Hello to console and Hello {name}")
        print(f"Hello to console is is your {email}")
        print(f"Hello to console it is your {name} HAHAHAHAHAHA")
        print(f"Hello to console and is your {name}")
        #hakerobebiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
        return render_template("login.html", name=name)
    
         


if __name__ == '__main__':
        app.run(debug=True)

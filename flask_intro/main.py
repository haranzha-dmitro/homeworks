from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/vegetables')
def get_vegetables():
    vegetables_list = ('beans', 'carrot', 'beetroot', 'cucumber')
    return render_template("vegetables.html", data=vegetables_list)
                                                                                                                    

@app.route('/fruits')
def get_fruits():
    fruits_list = ("melon", "apple", "strawberry", "grape")
    return render_template("fruits.html", data=fruits_list)


if __name__ == "__main__":
    app.run(debug=True)

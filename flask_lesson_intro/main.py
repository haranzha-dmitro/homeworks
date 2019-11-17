from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")

@app.route('/<item>')
def get_item_page(item):
    for product in get_data():
        if product['title'] == item:
            return render_template('item.html',
                                   title=item,
                                   item=item,
                                   text=product['text'],
                                   count=len(product['text']))
    else:
        return render_template("error404.html")

@app.route('/author_page')
def get_author_page():
    return render_template('/author.html')

if __name__ == "__main__":
    app.run(debug=True)

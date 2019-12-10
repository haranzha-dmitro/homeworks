from flask import Flask, render_template, session
from datetime import timedelta
from products.products import products
from supermarkets.supermarkets import supermarkets
from db.database import DB, test_DB
from models import Product, Supermarket


def db_create():
    DB['products'] = []
    DB['supermarkets'] = []


def fill_db():
    def add_product(data):
        DB['products'].append(Product(name=data.get('name'),
                                      description=data.get('description'),
                                      img_name=data.get('img_name'),
                                      price=data.get('price')
                                      )
                              )

    def add_market(data):
        DB['supermarkets'].append(Supermarket(name=data.get('name'),
                                              location=data.get('location'),
                                              img_name=data.get('img_name')
                                              )
                                  )

    for product in test_DB['products']:
        add_product(product)
    for market in test_DB['supermarkets']:
        add_market(market)


def app_create():
    db_create()
    fill_db()
    app = Flask(__name__, static_folder='home/static', template_folder='home/templates')
    app.config['SECRET_KEY'] = 'very_strong_secret_key'
    app.register_blueprint(supermarkets)
    app.register_blueprint(products)
    app.permanent_session_lifetime = timedelta(seconds=10)
    return app


app = app_create()


@app.route('/')
def get_home_page():
    session['login'] = 'ok'
    return render_template('home.html')


@app.route('/author')
def get_author_page():
    return render_template('author.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

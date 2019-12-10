import os

from flask import (Blueprint, render_template, request,
                   redirect, url_for, session)
from werkzeug.utils import secure_filename

from db.database import DB
from models import Product
from products.addprodform import AddProductForm

products = Blueprint('products', __name__,
                     url_prefix='/products',
                     template_folder='../products/templates',
                     static_folder='../products/static')


@products.route('/', methods=['GET'])
def get_all_products():
    products_all = [product.__dict__ for product in DB['products']]
    args = request.args.to_dict()
    return render_template('all_products.html',
                           products_all=products_all, args=args)


@products.route('/add', methods=['GET', 'POST'])
def show_add_product_form():
    form = AddProductForm()

    return render_template('addproduct.html', form=form)


@products.route('/submit', methods=['POST'])
def add_product():
    try:
        price = float(request.form.get('price'))
    except ValueError:
        return redirect(url_for('products.show_add_product_form'))

    if price > 0:
        data = request.form.to_dict()
        filename = None
        if request.files['img_name']:
            file = request.files['img_name']
            filename = secure_filename(file.filename)
            path_to_img = os.path.join('products/static',
                                       secure_filename(filename)
                                       )
            file.save(path_to_img)
        DB['products'].append(Product(name=data.get('name'),
                                      description=data.get('description'),
                                      img_name=filename,
                                      price=data.get('price')
                                      )
                              )
        return redirect(url_for('products.get_all_products'))
    else:
        return redirect(url_for('products.show_add_product_form'))


@products.route('/<uuid:uu_id>')
def show_product(uu_id):
    uu_id = str(uu_id)
    session[uu_id] = True
    products_all = [product.__dict__ for product in DB['products']]
    product_to_show = None
    for product in products_all:
        if uu_id in product.values():
            product_to_show = product
            session[product['id']] = True
    return render_template('product.html', product=product_to_show, title=product_to_show.get('name'))

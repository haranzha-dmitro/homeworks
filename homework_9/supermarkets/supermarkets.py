import os

from flask import Blueprint, render_template, request, url_for, redirect, session
from werkzeug.utils import secure_filename

from db.database import DB
from models import Supermarket
from supermarkets.addsupermarketform import AddMarketForm

supermarkets = Blueprint('supermarkets', __name__,
                         url_prefix='/supermarket',
                         template_folder='../supermarkets/templates',
                         static_folder='../supermarkets/static')


@supermarkets.route('/', methods=['GET'])
def get_all_supermarkets():
    markets_all = [market.__dict__ for market in DB['supermarkets']]
    args = request.args.to_dict()
    return render_template('all_supermarkets.html',
                           markets_all=markets_all, args=args)


@supermarkets.route('/add', methods=['GET', 'POST'])
def show_add_market_form():
    form = AddMarketForm()
    if form.validate_on_submit():
        data = request.form.to_dict()
        file = request.files['img_name']
        filename = secure_filename(file.filename)
        path_to_img = os.path.join('supermarkets/static',
                                   secure_filename(filename)
                                   )
        file.save(path_to_img)
        DB['supermarkets'].append(Supermarket(name=data.get('name'),
                                              location=data.get('location'),
                                              img_name=filename
                                              )
                                  )
        print(DB)
        print(filename)
        return redirect(url_for('supermarkets.get_all_supermarkets'))
    return render_template('addmarket.html', form=form)


@supermarkets.route('/<uuid:uu_id>')
def show_market(uu_id):
    uu_id = str(uu_id)
    markets_all = [market.__dict__ for market in DB['supermarkets']]
    market_to_show = None
    for market in markets_all:
        if uu_id in market.values():
            market_to_show = market
            session[market['id']] = True
    return render_template('supermarket.html', market=market_to_show, title=market_to_show.get('name'))

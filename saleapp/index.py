
from flask import render_template, request
from unicodedata import category

from saleapp import app

import utils



# Controller

@app.route("/")
def home():

    categories = utils.load_categories()
    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    prods = utils.load_products(kw=kw, cate_id=cate_id)

    return render_template("client/homepage.html", categories=categories, products=prods)


@app.route("/products")
def get_product_page():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')

    products = utils.load_products(cate_id, kw, from_price, to_price)
    return render_template("client/product.html", products=products)

@app.route("/category/<int:category_id>")
def get_category_page(category_id):
    cate = Category.query.get_or_404(category_id)
    products = utils.load_products(cate_id=category_id)

    return render_template('product.html', products=products)


@app.route("/product/<int:product_id>")
def get_product_detail_page(product_id):
    product = utils.get_product_by_id(product_id)
    categories = utils.load_categories()
    prods = utils.load_products()
    return render_template("client/detail.html", product = product, categories=categories, products=prods)


if __name__ == '__main__':
    from saleapp.admin import *

    app.run(debug=True)

from itertools import product

from flask import render_template, request
from saleapp import app
from unicodedata import category

import utils



# Controller? Java

@app.route("/")
def home():
    categories = utils.load_categories()

    return render_template("client/index.html", categories=categories)


@app.route("/products")
def get_product_page():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')

    products = utils.load_products(cate_id, kw, from_price, to_price)
    return render_template("client/product.html", products=products)


@app.route("/product/<int:product_id>")
def get_product_detail_page(product_id):
    product = utils.get_product_by_id(product_id)
    return render_template("client/product-detail.html", product = product)


if __name__ == '__main__':
    from saleapp.admin import *

    app.run(debug=True)

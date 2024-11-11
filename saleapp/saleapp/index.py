import math
from flask import render_template, request, redirect, url_for
from saleapp import app
import utils
import cloudinary.uploader

# Controller
@app.context_processor
def response_categories():
    return {
        'categories': utils.load_categories()
    }

@app.route("/")
def home():


    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    page = request.args.get('page', 1)

    prods = utils.load_products(kw=kw, cate_id=cate_id, page=int(page))
    counter = utils.count_product()

    return render_template("client/homepage.html",
                           products=prods,
                           page=int(page),
                           pages=math.ceil(counter/app.config['PAGE_SIZE']))


@app.route("/products")
def get_product_page():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    page = request.args.get('page', 1)

    products = utils.load_products(cate_id, kw, from_price, to_price, page=int(page))


    counter = utils.count_product()
    return render_template("client/product.html",
                           products=products,
                           page=int(page),
                           pages=math.ceil(counter/app.config['PAGE_SIZE']))

@app.route("/category/<int:category_id>")
def get_category_page(category_id):
    cate = Category.query.get_or_404(category_id)
    products = utils.load_products(cate_id=category_id)

    return render_template('product.html', products=products)


@app.route("/product/<int:product_id>")
def get_product_detail_page(product_id):
    product = utils.get_product_by_id(product_id)

    prods = utils.load_products()
    return render_template("client/detail.html", product = product, products=prods)


@app.route('/login', methods=['get', 'post'])
def get_login_page():
    return render_template('client/login.html')

@app.route('/register', methods=['get', 'post'])
def get_register_page():
    error_message = ''
    if request.method.__eq__('POST'):
        name = request.form.get('fullname')
        username = request.form.get('phone')
        password = request.form.get('password')
        email = request.form.get('email')
        name = request.form.get('fullname')
        confirm_password = request.form.get('confirmPassword')
        avatar_path = None

        try:
            if password.strip().__eq__(confirm_password.strip()):
                avatar = request.files.get('avatar')
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    print(res)
                    avatar_path = res['secure_url']

                utils.add_user(name=name, username=username, password=password, email=email, avatar=avatar_path)
                return redirect(url_for('get_login_page'))
            else:
                error_message = 'Mật khẩu không khớp!!!'
        except Exception as ex:
            error_message = 'Lỗi nè: ' + str(ex)



    return render_template('client/register.html', error_message=error_message)



if __name__ == '__main__':
    from saleapp.admin import *

    app.run(debug=True)

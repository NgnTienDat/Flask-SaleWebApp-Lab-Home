from wtforms.validators import email

from saleapp import app, db
from saleapp.models import Category, Product, User
import hashlib

# Service
#
# def read_json(path):
#     with open(path, "r") as f:
#         return json.load(f)

def load_categories():
    # return read_json(os.path.join(app.root_path, 'data/categories.json'))      -> get data from JSON
    return Category.query.order_by('id').all()   # Get data from database

def load_products(cate_id = None, kw = None, from_price = None, to_price = None, page=1):
    # products = read_json(os.path.join(app.root_path, 'data/product.json'))
    products = Product.query.filter(Product.active.__eq__(True))

    if cate_id:
        # products = [p for p in products if p['category_id']==int(cate_id)]
        products = products.filter(Product.category_id == int(cate_id))

    if kw:
        # products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
        products =products.filter(Product.name.contains(kw))

    if from_price:
        # products = [p for p in products if p['price'] >= float(from_price)]
        products = products.filter(Product.price >= float(from_price))

    if to_price:
        # products = [p for p in products if p['price'] <= float(to_price)]
        products = products.filter(Product.price <= float(to_price))

    page_size = app.config['PAGE_SIZE']
    start = (page-1)*page_size
    end = start+page_size

    return products.slice(start, end).all()


def count_product():
    return Product.query.filter(Product.active.__eq__(True)).count()

def get_product_by_id(product_id):
    # products = read_json(os.path.join(app.root_path, 'data/product.json'))
    # for p in products:
    #     if p['id']==product_id:
    #         return
    return Product.query.get(product_id)


def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(), username=username.strip(), password=password,
                email = kwargs.get('email'),
                avatar = kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()
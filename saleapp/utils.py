
from saleapp.models import Category, Product


# Service
#
# def read_json(path):
#     with open(path, "r") as f:
#         return json.load(f)

def load_categories():
    # return read_json(os.path.join(app.root_path, 'data/categories.json'))      -> get data from JSON
    return Category.query.order_by('id').all()   # Get data from database

def load_products(cate_id = None, kw = None, from_price = None, to_price = None):
    # products = read_json(os.path.join(app.root_path, 'data/product.json'))
    products = Product.query

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

    return products.all()

def get_product_by_id(product_id):
    # products = read_json(os.path.join(app.root_path, 'data/product.json'))
    # for p in products:
    #     if p['id']==product_id:
    #         return
    return Product.query.get(product_id)
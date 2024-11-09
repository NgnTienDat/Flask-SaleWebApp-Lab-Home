from saleapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product
admin = Admin(app=app, name='E-commerce Administration', template_mode='bootstrap4')

class ProductView(ModelView):
    # Hiển thị category dưới dạng tên thay vì khóa ngoại ID
    column_list = ['name', 'description', 'price', 'image', 'active', 'created_date', 'category_id'] # Thêm 'category'
    form_columns = ['name', 'description', 'price', 'image', 'active', 'created_date', 'category_id']  # Để người dùng chọn category từ danh sách
    column_labels = {
        'category': 'Category'
    }

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))

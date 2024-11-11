from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cloudinary

app = Flask(__name__)
app.secret_key = '^&*)%T*O&T*^&%)*^T%*&T)*O&RTO)(*FGKYTDFHKTFGK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tiendatmySQL964%40@localhost/labsaledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['PAGE_SIZE'] = 8

db = SQLAlchemy(app=app)

cloudinary.config(
    cloud_name = 'dq94qmefz',
    api_key = '876776184315666',
    api_secret = 'XNP84wQu2yfxt1gjm59KdGMBxJk',
)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key='^&*)%T*O&T*^&%)*^T%*&T)*O&RTO)(*FGKYTDFHKTFGK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tiendatmySQL964%40@localhost/labsaledb?charset=utf8mb4'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)
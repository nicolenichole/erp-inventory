# app/models.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), unique=True, nullable=False)
    location = db.Column(db.String(128))

class StockLot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)

    product = db.relationship('Product', backref='lots')
    warehouse = db.relationship('Warehouse', backref='lots')

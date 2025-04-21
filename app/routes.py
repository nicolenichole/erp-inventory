# app/routes.py
from flask import request, jsonify, Blueprint
from .models import db, Product, Warehouse, StockLot

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    p = Product(sku=data['sku'], name=data['name'])
    db.session.add(p); db.session.commit()
    return jsonify(id=p.id), 201

@bp.route('/stock', methods=['POST'])
def adjust_stock():
    data = request.json
    lot = StockLot.query.filter_by(
        product_id=data['product_id'],
        warehouse_id=data['warehouse_id']
    ).first()
    if not lot:
        lot = StockLot(**data)
    else:
        lot.quantity += data.get('quantity', 0)
    db.session.add(lot); db.session.commit()
    return jsonify(id=lot.id, qty=lot.quantity)

@bp.route('/stock/<int:product_id>')
def get_stock(product_id):
    totals = db.session.query(
        StockLot.warehouse_id,
        db.func.sum(StockLot.quantity)
    ).filter_by(product_id=product_id).group_by(StockLot.warehouse_id).all()
    return jsonify({wh: qty for wh, qty in totals})


from flask import Blueprint, jsonify, request

# Models
from models.ProductModel import ProductModel

main = Blueprint('product_blueprint', __name__)

@main.route('/')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_single_product(id):
    try:
        product = ProductModel.get_product(id)
        if product is None:
            return jsonify({'message': "Value Not Found"}), 404
        return jsonify(product)
    except Exception as ex:
        
        return jsonify({'message': str(ex)}), 500  
    

@main.route('/', methods=['POST'])
def create_product():
    try:
        
        return jsonify({'new product id': ProductModel.create_product(request.json)})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  

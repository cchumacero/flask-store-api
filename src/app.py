from flask import Flask
from config import config

app = Flask(__name__)
app.json.sort_keys = False # Config line to not order the json output

# Routes
from routes import Product

def page_not_found(error):
    return "<h1>Not Found Page</h1>", 404



if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(Product.main, url_prefix='/api/v1/products')
    
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()

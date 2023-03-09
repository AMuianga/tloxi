from flask import Flask

from config import Config
from .extensions import db, bcrypt

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    bcrypt.init_app(app)

    
    # Register blueprints here
    from .main.routes import main
    app.register_blueprint(main, url_prefix='/')

    from .auth.routes import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from .carts.routes import carts
    app.register_blueprint(carts, url_prefix='/carts')
    
    from .products.routes import products
    app.register_blueprint(products, url_prefix='/products')

    return app



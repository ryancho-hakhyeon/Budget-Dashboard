from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aslkdjflasdflkjasfl'

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint()
    # app.register_blueprint()
    # app.register_blueprint()
    # app.register_blueprint()

    return app
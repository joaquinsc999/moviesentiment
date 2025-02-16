from app.routes.sentiment_routes import sentiment_routes

def register_routes(app):
    app.register_blueprint(sentiment_routes)

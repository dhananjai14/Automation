from flask_cors import CORS
from flask import Flask, request, jsonify
from routes.routes import api_blueprint
app = Flask(__name__)
CORS(app)

app.register_blueprint(api_blueprint, url_prefix='/excel')

if __name__ == "__main__":
    app.run()
import os
from flask import Blueprint, jsonify, request
from utils.logger import get_logger
logging = get_logger()

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/health", methods=["GET"])
def health_check():
    """
    Route: /health [GET]
    Health check endpoint to verify if the service is running.
    Returns a JSON response with status 200 if the service is up.
    """
    logging.info("Inside the route /health")
    # logging.info("Health check successful")
    return jsonify({ "status": 200, "result": "Service is running"}), 200



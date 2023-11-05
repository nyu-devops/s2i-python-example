"""
Simple Flask App
"""
import os
from flask import Flask

PORT = int(os.getenv('PORT', '8080'))

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Home Page"""
    app.logger.info("Request for home page...")
    return {"name": "Flask App"}, 200


@app.route('/health', methods=['GET'])
def health():
    """Health Check"""
    return {"status": "OK"}, 200


@app.route('/hello', methods=['GET'])
def hello():
    """Send back Hello world"""
    app.logger.info("Request for Hello message...")
    return {"message": "Hello World"}, 200


############################################################
#  M A I N   P R O G R A M
############################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

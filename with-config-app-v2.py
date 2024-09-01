from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

# Load ConfigMap data as environment variables
data_json = os.getenv('DATA_LIST', '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}, {"id": 3, "name": "Item 3"}]')
data_list = json.loads(data_json)

# Health Check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

# Data route
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_list)

# Kubernetes route (something playful)
@app.route('/k8s', methods=['GET'])
def kubernetes_playful():
    message = app.config.get('WELCOME_MESSAGE', 'Welcome to the world of Kubernetes!')
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

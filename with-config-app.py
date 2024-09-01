from flask import Flask, jsonify
import os

app = Flask(__name__)

# Load ConfigMap and Secret values
app.config['WELCOME_MESSAGE'] = os.getenv('WELCOME_MESSAGE', 'Default welcome message')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'DefaultSecretKey')

# Health Check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

# Data route
@app.route('/data', methods=['GET'])
def get_data():
    data = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'}
    ]
    return jsonify(data)

# Kubernetes route (something playful)
@app.route('/k8s', methods=['GET'])
def kubernetes_playful():
    message = app.config['WELCOME_MESSAGE']
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

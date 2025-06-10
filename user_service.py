from flask import Flask, request, jsonify
from config import Config
from services import UserService

app = Flask(__name__)
cfg = Config()
app.config['SECRET_KEY'] = cfg.get('SECRET_KEY')
user_service = UserService(cfg)

# Crear usuario
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    uid = user_service.create_user(data['name'], data['email'])
    return jsonify({"id": uid}), 201

# Listar todos los usuarios
@app.route('/users', methods=['GET'])
def list_users():
    users = user_service.list_all_users()
    return jsonify(users), 200

# Obtener un usuario por ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if not user:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user), 200

# Eliminar un usuario por ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)

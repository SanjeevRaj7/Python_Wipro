#implement the assignment which was given to mysql write the api for nosql and test the same

from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Database
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb3"]  # Database name
mycol = db["emp"]  # Table name

#1.CREATE USER
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json #request api to inset data

    user_data = {
        "name": data['name'],
        "email": data['email'],
        "job": data['job']
    }

    r = mycol.insert_one(user_data)
    user_id = r.inserted_id

    return jsonify({"message": "User created", "user_id": str(user_id)}), 201


# 2. Get all users
@app.route('/users', methods=['GET'])
def get_users():
    # Fetch all users from MongoDB
    users = mycol.find()
    users1 = [{"id": str(data["_id"]), "name": data["name"], "email": data["email"], "job": data["job"]} for data in
                  users]

    return jsonify(users1)

#3.update a user
@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json #json data from api request
    r=mycol.update_one({"_id":ObjectId(user_id)},{"$set":{"name":data["name"],"email":data["email"],"job":data["job"]}})
    if r.matched_count == 0:
        return jsonify({'error': 'user not found'}),404
    return jsonify({"message":"user updated successfully"})

#3. DELETE A USER
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    r = mycol.delete_one({"_id": ObjectId(user_id)}) #delete user using objectid

    if r.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
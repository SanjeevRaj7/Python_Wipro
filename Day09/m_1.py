import pymongo
from bson import ObjectId
from flask import Flask, request, jsonify
#from bson import ObjectId

app = Flask(__name__)

@app.route('/add_users', methods=['POST'])
def add_user():
    mycnx = pymongo.MongoClient("mongodb://localhost:27017/")
    myDatabase = mycnx['mydb']
    mycol = myDatabase['users']
    data = request.json #json data from api request
    r=mycol.insert_one(data)#insert data into MongoDB
    user_id= r.inserted_id

    return jsonify({'message': 'user added successfully', 'user_id': str(user_id)})


@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    mycnx = pymongo.MongoClient("mongodb://localhost:27017/")
    myDatabase = mycnx['mydb']
    mycol = myDatabase['users']
    data = request.json #json data from api request
    # mycol.update_one(data) #insert data into MongoDB
    r=mycol.update_one({"_id":ObjectId(user_id)},{"$set":{"name":data["name"],"age":data["age"]}})
    if r.matched_count == 0:
        return jsonify({'error': 'user not found'}),404
    return jsonify({"message":"user updated successfully"})

@app.route('/get_users', methods=['GET'])
def get_users():
    mycnx = pymongo.MongoClient("mongodb://localhost:27017/")
    myDatabase = mycnx['mydb']
    mycol = myDatabase['users']
    #users = list(mycol.find({},{"_id":0})) #fetch all users excluding id
    users=[{"id":str(data["_id"]),"name":data['name'],"age":data['age']} for data in mycol.find()]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
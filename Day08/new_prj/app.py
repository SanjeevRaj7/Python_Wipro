from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "Sanjeev",
    "password": "Silusanju@123",
    "database": "test_db"
}

# Establish Database Connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# REST API Endpoints

# 1. Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
   

    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = connection.cursor()

    query = "INSERT INTO users (name, email, job) VALUES (%s, %s, %s)"
    values = (data['name'], data['email'], data['job'])

    cursor.execute(query, values)
    connection.commit()
    user_id = cursor.lastrowid

    cursor.close()
    connection.close()
    return jsonify({"message": "User created", "user_id": user_id}), 201

# 2. Get all users
@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = connection.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    users = [{"id": row[0], "name": row[1], "email": row[2], "job": row[3]} for row in rows]

    cursor.close()
    connection.close()
    return jsonify(users)

# 3. Update a user (PUT)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = connection.cursor()

    query = "UPDATE users SET name = %s, email = %s, job = %s WHERE id = %s"
    values = (data['name'], data['email'], data['job'], user_id)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({"message": "User updated"})

# 4. Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = connection.cursor()

    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({"message": "User deleted"})

# 5. GET A SINGLE USER
@app.route('/users/<int:user_id>', methods=['GET'])
def single_user(user_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    row= cursor.fetchone()
    users={"id": row[0], "name": row[1], "email": row[2], "job": row[3]}
   # cursor.close()
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify(users)



if __name__ == '__main__':
    app.run(debug=True)

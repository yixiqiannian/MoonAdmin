from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 数据库连接配置
def create_connection():
    return mysql.connector.connect(
        host='mysql.sqlpub.com',
        user='cangshu',
        password='eECZ13LELV1Ubsgv',
        database='cangshu'
    )

@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM moon_users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if user and user['password'] == password:  # 这里可以使用 bcrypt 进行密码验证
        # 获取上次登录时间
        last_login = user['last_login']
        
        # 更新最后登录时间为当前时间
        cursor.execute("UPDATE moon_users SET last_login = NOW() WHERE id = %s", (user['id'],))
        connection.commit()
        
        return jsonify({
            'code': 200,
            'message': '登录成功',
            'data': {
                'id': user['id'],
                'username': user['username'],
                'email': user['email'],
                'avatar': user['avatar'],
                'role': user['role'],
                'token': user['token'],  # 这里可以生成 JWT token
                'last_login': last_login  # 返回上次登录时间
            }
        })
    
    return jsonify({
        'code': 401,
        'message': '用户名或密码错误'
    })

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM moon_users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': {
                'id': user['id'],
                'username': user['username'],
                'email': user['email'],
                'avatar': user['avatar'],
                'role': user['role']
            }
        })
    return jsonify({
        'code': 404,
        'message': '用户不存在'
    })

@app.route('/api/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    data = request.get_json()
    cursor.execute("UPDATE moon_users SET username = %s, email = %s, avatar = %s WHERE id = %s",
                   (data.get('username'), data.get('email'), data.get('avatar'), user_id))
    connection.commit()
    
    return jsonify({
        'code': 200,
        'message': '更新成功'
    })

@app.route('/api/user/<user_id>/contacts', methods=['GET'])
def get_user_contacts(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM moon_user_contacts WHERE user_id = %s", (user_id,))
    contacts = cursor.fetchone()
    
    if contacts:
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': contacts
        })
    return jsonify({
        'code': 404,
        'message': '用户联系方式不存在'
    })

@app.route('/api/user/<user_id>/contacts', methods=['PUT'])
def update_user_contacts(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    data = request.get_json()
    cursor.execute("UPDATE moon_user_contacts SET github = %s, qq = %s, wechat = %s,about_me = %s WHERE user_id = %s ",
                   (data.get('github'), data.get('qq'), data.get('wechat'),data.get('about_me'), user_id))
    connection.commit()
    
    return jsonify({
        'code': 200,
        'message': '联系方式更新成功'
    })

@app.route('/api/user/<user_id>/username', methods=['PUT'])
def update_username(user_id):
    data = request.get_json()
    new_username = data.get('username')
    
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("UPDATE moon_users SET username = %s WHERE id = %s", (new_username, user_id))
    connection.commit()
    
    return jsonify({
        'code': 200,
        'message': '用户名更新成功'
    })

@app.route('/api/user/<user_id>/username', methods=['GET'])
def get_username(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT username FROM moon_users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': user['username']
        })
    return jsonify({
        'code': 404,
        'message': '用户不存在'
    })

@app.route('/api/user/<user_id>/avatar', methods=['PATCH'])
def update_avatar(user_id):
    if 'avatar' not in request.form:
        return jsonify({'code': 400, 'message': '没有上传头像 URL'}), 400

    avatar_url = request.form['avatar']
    if not avatar_url:
        return jsonify({'code': 400, 'message': '头像 URL 不能为空'}), 400

    # 更新数据库中的头像路径
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE moon_users SET avatar = %s WHERE id = %s", (avatar_url, user_id))
    connection.commit()

    return jsonify({'code': 200, 'message': '头像更新成功', 'data': avatar_url})

@app.route('/api/user/<user_id>/avatar', methods=['GET'])
def get_avatar(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT avatar FROM moon_users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': user['avatar']
        })
    return jsonify({
        'code': 404,
        'message': '用户不存在'
    })

@app.route('/api/user/<user_id>/password', methods=['PUT'])
def update_password(user_id):
    data = request.get_json()
    new_password = data.get('password')
    
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("UPDATE moon_users SET password = %s WHERE id = %s", (new_password, user_id))
    connection.commit()
    
    return jsonify({
        'code': 200,
        'message': '密码更新成功'
    })

@app.route('/api/user/<user_id>/last_login', methods=['GET'])
def get_last_login(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT last_login FROM moon_users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': user['last_login']
        })
    return jsonify({
        'code': 404,
        'message': '用户不存在'
    })

@app.route('/api/user/<user_id>/email', methods=['PUT'])
def update_email(user_id):
    data = request.get_json()
    new_email = data.get('email')
    
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("UPDATE moon_users SET email = %s WHERE id = %s", (new_email, user_id))
    connection.commit()
    
    return jsonify({
        'code': 200,
        'message': '邮箱更新成功'
    })

@app.route('/api/user/<user_id>/email', methods=['GET'])
def get_email(user_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT email FROM moon_users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    if user:
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': user['email']
        })
    return jsonify({
        'code': 404,
        'message': '用户不存在'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from profiles import profile
from modal.modals import Profile, Addr
from flask import request, jsonify
from modal.database import db, MYSQL_DB, MYSQL_PASSWORD, MYSQL_USER, MYSQL_HOST, MYSQL_INSTANCE_CONNECTION
from datetime import datetime
import bcrypt
from flask_login import login_user


@profile.route("/welcome", methods=["GET"])
def welcome_result():
    return jsonify({
        "message":"hello welcomes you",
        "db":MYSQL_DB,
        "user":MYSQL_USER,
        "password":MYSQL_PASSWORD,
        "host":MYSQL_HOST,
        "instance":MYSQL_INSTANCE_CONNECTION
    })


@profile.route('/create', methods=['POST'])
def create_profile():
    data = request.get_json()
    try:
        new_profile = Profile(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            age=data['age'],
            sex=data['sex']
        )
        db.session.add(new_profile)
        db.session.commit()
        return f"Profile created for {new_profile.username} with id {new_profile.id}", 201
    except Exception as e:
        return f"invalid entry {e}", 400    
   
@profile.post('/login')
def initiate_login():
    data = request.get_json()
    try:
        profile = Profile.query.filter_by(email=data['email']).first()
     
        if profile and bcrypt.checkpw(data['password'].encode('utf-8'), profile.password.encode('utf-8')):
            login_user(profile)
            return jsonify({
                "message":"User Logged in!"
            }), 200
        else:
            return jsonify({"error": "User not found"}), 404

   
    except Exception as e:
        return e
   

@profile.post('/update/<int:user_id>')
def update_profile(user_id):
    data = request.get_json()
    try:
        user = Profile.query.get(user_id)
        if not user:
            return f"User with id {user_id} not found", 404
       
        if data['username']:
            user.username = data['username']
        if data['age']:
            user.age = data['age']
        if data['sex']:
            user.sex=data['sex']

        db.session.commit()

        return f"Profile updated for user id {user_id}", 200

    except Exception as e:
        return f"invalid entry {e}", 400    
   

@profile.post('/address/create/<int:user_id>')
def create_user_address(user_id):
    data = request.get_json()
    try:
        user = Profile.query.get(user_id)
        if not user:
            return f"User with id {user_id} not found", 404
       
        new_address = Addr(
            address=data['address'],
            city=data['city'],
            state=data['state'],
            pincode=data['pincode'],
            profile=user
        )
        db.session.add(new_address)
        db.session.commit()
        return f"Address created for user id {user_id} with address id {new_address.id}", 201
    except Exception as e:
        return f"invalid entry {e}", 400    

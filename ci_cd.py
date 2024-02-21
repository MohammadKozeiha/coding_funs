from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
api = Api(app)
db = SQLAlchemy(app)

# Define a simple User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
db.create_all()

# Resource to handle user registration
class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

# Resource to get a list of all users
class UserList(Resource):
    def get(self):
        users = User.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return {'users': user_list}

# Add resources to the API
api.add_resource(UserRegistration, '/api/register')
api.add_resource(UserList, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)
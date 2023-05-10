from flask import jsonify, request, current_app
from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from cdmsapp.schemas import UserSchema
from cdmsapp.models import UserModel

from cdmsapp.routes.password_email import send_email12


blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.find_by_username(user_data["username"]):
            abort(400, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        user.save_to_db()

        return {"message": "User created successfully."}, 201



@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.find_by_username(user_data["username"])

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")

@blp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    # current_user = get_jwt_identity()
    return jsonify(logged_in_as="Amar"), 200
    



@blp.route("/user/<int:user_id>", methods=["GET"])
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful
    when we are manipulating data regarding the users.
    """

    @blp.response(200, UserSchema)
    @jwt_required(refresh=True)
    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            abort(404, message="User not found.")
        return user

    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            abort(404, message="User not found.")
        user.delete_from_db()
        return {"message": "User deleted."}, 200


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200

@blp.route('/users')
class UsersAll(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        users = UserModel.get_all_user()
        return users







    

 


# class UserLogout(MethodView):
#     # @jwt_required(refresh=True)
#     def post(self):
#         jti = get_jwt()["jti"]
#         tokenBlocklist = TokenBlocklistModel(
#             jti = jti,
#             created_at = datetime.now()
#         )
#         tokenBlocklist.save_to_db()
#         return {"message": "Successfully logged out"}, 200




@blp.route("/forget_password", methods=["POST"])
def forget_password():
    data = request.get_json()
    username = data.get("username")
    if not username:
        abort(400, message="Username is required")

  
    user = UserModel.find_by_username(username=username)
    if not user:
        abort(404, message="User not found")

    
    token = user.generate_reset_password_token()

    # reset_password_url = f"{current_app.config['FRONTEND_URL']}/passwordreset/{token}"reset
    reset_password_url = f"http://16.170.207.211/passwordreset/{token}"

    recipients = [user.username]
    body = f"Hi {user.username},\n\nPlease use the following link to reset your password:\n\n{reset_password_url}\n\nThanks,\nThe Wasca Team"
   
    send_email12('Password reset requested', 'noreply@example.com', recipients, body)

    return jsonify({"message": "Password reset email sent"}), 200


@blp.route("/reset_password/<token>", methods=['POST','GET'])
def reset_password(token):
    user_id = UserModel.verify_reset_password_token(token)
    if not user_id:
        abort(400, message="Invalid or expired token")

    user = UserModel.query.get(user_id)
    if not user:
        abort(404, message="User not found")

    data = request.get_json()
    new_password = data.get("password")

    if new_password:
        user.password = pbkdf2_sha256.hash(new_password)
        user.save_to_db()
        return jsonify({"message": "Password reset successfully"}), 200
    else:
        abort(400, message="New password is required.")



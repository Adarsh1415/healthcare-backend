from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from services import admin_service

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

def is_admin():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return user and user.role == "admin"


# Departments
@admin_bp.route("/departments", methods=["POST"])
@jwt_required()
def create_department():
    if not is_admin():
        return {"message": "Access denied"}, 403
    data = request.get_json()
    return admin_service.create_department(data.get("name"))


@admin_bp.route("/departments", methods=["GET"])
@jwt_required()
def list_departments():
    if not is_admin():
        return {"message": "Access denied"}, 403
    return admin_service.list_departments()


@admin_bp.route("/departments/<int:department_id>/doctors", methods=["GET"])
@jwt_required()
def list_doctors_by_department(department_id):
    if not is_admin():
        return {"message": "Access denied"}, 403
    return admin_service.list_doctors_by_department(department_id)


# Doctors
@admin_bp.route("/doctors", methods=["POST"])
@jwt_required()
def onboard_doctor():
    if not is_admin():
        return {"message": "Access denied"}, 403
    data = request.get_json()
    return admin_service.onboard_doctor(
        data.get("username"),
        data.get("password"),
        data.get("department_id")
    )


@admin_bp.route("/doctors", methods=["GET"])
@jwt_required()
def list_doctors():
    if not is_admin():
        return {"message": "Access denied"}, 403
    return admin_service.list_doctors()


@admin_bp.route("/doctors/<int:doctor_id>", methods=["PUT"])
@jwt_required()
def assign_doctor(doctor_id):
    if not is_admin():
        return {"message": "Access denied"}, 403
    department_id = request.get_json().get("department_id")
    return admin_service.assign_doctor_to_department(doctor_id, department_id)

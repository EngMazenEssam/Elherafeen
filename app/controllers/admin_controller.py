from flask import Blueprint, redirect, url_for, flash
from app.services.request_service import RequestService

admin_bp = Blueprint("admin", __name__)
service = RequestService()

@admin_bp.route("/admin/approve/<request_id>", methods=["POST"])
def approve(request_id):
    try:
        service.approve(request_id)
        flash("Request approved", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("admin.requests"))

@admin_bp.route("/admin/reject/<request_id>", methods=["POST"])
def reject(request_id):
    try:
        service.reject(request_id)
        flash("Request rejected", "warning")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("admin.requests"))

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.seller_service import SellerService

seller_bp = Blueprint("seller", __name__, url_prefix="/seller")
service = SellerService()

@seller_bp.route("/", methods=["GET"])
def dashboard():
    seller_id = session.get("user_id", "seller_001") 
    
    data = service.get_dashboard_data(seller_id)
    return render_template("seller/dashboard.html", 
                           pending_products=data["pending"], 
                           approved_products=data["approved"])

@seller_bp.route("/submit", methods=["POST"])
def submit_product():
    seller_id = session.get("user_id", "seller_001")
    
    try:
        service.submit_product(request.form, request.files, seller_id)
        flash("Product submitted successfully for approval!", "success")
    except Exception as e:
        flash(f"Error submitting product: {str(e)}", "error")
        
    return redirect(url_for("seller.dashboard"))

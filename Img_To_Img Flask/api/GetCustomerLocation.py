# api/getCustomerLocation.py

from flask import Blueprint, request, jsonify
from geopy.geocoders import Nominatim

# 将 URL 前缀放到 blueprint 定义里
location_bp = Blueprint("location_bp", __name__, url_prefix="/location")

# POST /location/get
@location_bp.route("/get", methods=["POST"])
def get_location():
    """
    请求：{ "latitude": float, "longitude": float }
    返回：{ "latitude": ..., "longitude": ..., "address": "..." }
    """
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    if lat is None or lon is None:
        return jsonify({"error": "Missing coordinates"}), 400

    geolocator = Nominatim(user_agent="")#写自己邮箱
    location = geolocator.reverse((lat, lon), language="zh")

    return jsonify({
        "latitude": lat,
        "longitude": lon,
        "address": location.address if location else "无法识别位置"
    })



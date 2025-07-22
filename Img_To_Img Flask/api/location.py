from flask import Blueprint, jsonify, request
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

location_api=Blueprint('location',__name__)

@location_api.route("/get",methods=['GET'])  #获取地理位置
def get_location():
    locations = [[-1,-1],[23.051,113.4011],[23.0545,113.398],[23.05379,113.397],[23.05037,113.39760],
                 [23.049167,113.398333],[23.048611,113.398611],[23.048889,113.400000],[23.051000,113.397222],
                 [23.048611,113.399167]]
    #1.湖边 2.二饭 3.麦当劳 4.三饭 5.教学区篮球场 6.教学区田径场 7.图书馆 8.一饭 9.音乐厅

    geolocator = Nominatim(
        user_agent="1486526957@qq.com",
        timeout=10  # 超时时间设为10秒
    )
    reverse_geocode = RateLimiter(geolocator.reverse, min_delay_seconds=1)

    data = request.args.to_dict()
    index = int(data.get('location'))
    lat = locations[index][0]
    lon = locations[index][1]

    if not lat or not lon:
        return jsonify({"error": "Missing coordinates"}), 400

    location = reverse_geocode((lat, lon), language='zh')

    return jsonify({
        "latitude": lat,
        "longitude": lon,
        "address": location.address if location else "无法识别位置"
    }),200
"""
简易地图接口：返回一段完整的 Folium‑HTML，可被前端 iframe 引用

from flask import Blueprint, Response
import folium
from image import map_type

map_bp = Blueprint("map", __name__, url_prefix="/map")
@map_bp.get("/")
def view_map():
    m = folium.Map(location=[23.048056, 113.402222], zoom_start=17)
    folium.Marker([23.048056, 113.402222], popup="华工").add_to(m)
    return Response(m.get_root().render(), mimetype="text/html")
"""


from flask import Blueprint, Response
import folium
from mapper.record_to_image import RecordToImage as mapperRecordToImage
from mapper.image import Image as mapperImage
from mapper.location import Location as mapperLocation  # 需要通过类型编号查位置
map_bp = Blueprint("map", __name__, url_prefix="/map")

@map_bp.route("/")
def view_map_default():#默认图
    m = folium.Map(location=[23.048056, 113.402222], zoom_start=17)
    folium.Marker([23.048056, 113.402222], popup="华工").add_to(m)
    return Response(m.get_root().render(), mimetype="text/html")

@map_bp.route("/record/<int:record_id>")
def view_map(record_id):#根据 record_id 展示图片对应位置
    m = folium.Map(location=[23.048056, 113.402222], zoom_start=17)

    connections = mapperRecordToImage.findByrecordId(record_id)
    for i, con in enumerate(connections):
        image = mapperImage.findById(con.image_id)
        category = image.category
        location = mapperLocation.findByType(category)  # category 是图片的分类ID

        if location and location.latitude != "-1" and location.longitude != "-1":
            folium.Marker(
                [float(location.latitude), float(location.longitude)],
                popup=f"相似图片 {i + 1}: {image.image}"
            ).add_to(m)

    return Response(m.get_root().render(), mimetype="text/html")

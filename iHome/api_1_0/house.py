# -*- coding:utf-8 -*-
# 实现房屋模块接口


from . import api
from iHome.models import Area, House, Facility
from flask import current_app, jsonify, request, g, session
from iHome.utils.response_code import RET
from iHome.utils.common import login_required
from iHome import db


@api.route('/houses/image', methods=['POST'])
@login_required
def upload_house_image():
    """发布房屋图片
    0.判断用户是否是登录 @login_required
    1.接受参数：image_data, house_id， 并做校验
    2.使用house_id查询house模型对象数据，因为如果查询不出来，就不需要上传图片了
    3.调用上传图片的工具方法，发布房屋图片
    4.将图片的七牛云的key,存储到数据库
    5.响应结果：上传的房屋图片，需要立即刷新出来
    """

    # 1.接受参数：image_data, house_id， 并做校验

    # 2.使用house_id查询house模型对象数据，因为如果查询不出来，就不需要上传图片了

    # 3.调用上传图片的工具方法，发布房屋图片

    # 4.将图片的七牛云的key,存储到数据库

    # 选择一个图片，作为房屋的默认图片

    # 5.响应结果：上传的房屋图片，需要立即刷新出来


@api.route('/houses', methods=['POST'])
@login_required
def pub_house():
    """发布新房源
    0.判断用户是否登录 @login_required
    1.接受所有参数,并判断是否缺少
    2.校验参数：price / deposit， 需要用户传入数字
    3.实例化房屋模型对象，并给属性赋值
    4.保存到数据库
    5.响应结果
    """

    # 1.接受所有参数,并判断是否缺少
    json_dict = request.json

    title = json_dict.get('title')
    price = json_dict.get('price')
    address = json_dict.get('address')
    area_id = json_dict.get('area_id')
    room_count = json_dict.get('room_count')
    acreage = json_dict.get('acreage')
    unit = json_dict.get('unit')
    capacity = json_dict.get('capacity')
    beds = json_dict.get('beds')
    deposit = json_dict.get('deposit')
    min_days = json_dict.get('min_days')
    max_days = json_dict.get('max_days')

    if not all([title, price, address, area_id, room_count, acreage, unit, capacity, beds, deposit, min_days, max_days]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数缺失')

    # 2.校验参数：price / deposit， 需要用户传入数字
    # 提示：在开发中，对于像价格这样的浮点数，不要直接保存浮点数，因为有精度的问题，一般以分为单位
    try:
        price = int(float(price) * 100)  # 0.1元 ==> 10分
        deposit = int(float(deposit) * 100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数格式错误')

    # 3.实例化房屋模型对象，并给属性赋值
    house = House()
    house.user_id = g.user_id
    house.area_id = area_id
    house.title = title
    house.price = price
    house.address = address
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days

    # 处理房屋的设施 facilities = [2,4,6]
    facilities = json_dict.get('facility')
    # 查询出被选中的设施模型对象
    house.facilities = Facility.query.filter(Facility.id.in_(facilities)).all()

    # 4.保存到数据库
    # try:
    #     db.session.add(house)
    #     db.session.commit()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     db.session.rollback()
    #     return jsonify(errno=RET.DBERR, errmsg='发布新房源失败')

    # 5.响应结果
    return jsonify(errno=RET.OK, errmsg='发布新房源成功', data={'house_id': house.id})


@api.route('/areas')
def get_areas():
    """提供城区信息
    1.查询所有的城区信息
    2.构造响应数据
    3.响应结果
    """

    # 1.查询所有的城区信息 areas == [Area,Area,Area,...]
    try:
        areas = Area.query.all()
    except Exception as e:
        current_app.logger.errno(e)
        return jsonify(errno=RET.DBERR, errmsg='查询城区信息失败')

    # 2.构造响应数据
    area_dict_list = []
    for area in areas:
        area_dict_list.append(area.to_dict())

    # 3.响应结果
    return jsonify(errno=RET.OK, errmsg='OK', data=area_dict_list)
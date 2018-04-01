# -*- coding:utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    """加载配置 所有的配置信息都写在这个类里面"""

    # 开启调试模式
    DEBUG = True

    # 秘钥
    SECRET_KET = 'jAqmDcz+U1SPDSBaZUT5q+mewqM8qabEKlJ5D5ohPV5GLJUMm3zjxg13N3GVUM32'

    # 配置mysql数据库: 开发中使用真实IP
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_07'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库: 开发中使用真实IP
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 创建连接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF保护
CSRFProtect(app)

# 创建脚本管理器对象
manager = Manager(app)

# 让app和db在迁移时建立关联
Migrate(app, db)
# 将数据库迁移脚本添加到脚本管理器
manager.add_command('db', MigrateCommand)


@app.route('/', methods=['GET', 'POST'])
def index():

    # 测试redis数据库
    redis_store.set('name', 'sz07')

    return 'index'


if __name__ == '__main__':
    # app.run()

    manager.run()
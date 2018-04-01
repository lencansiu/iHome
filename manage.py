# -*- coding:utf-8 -*-


from flask import Flask


class Config(object):
    """加载配置 所有的配置信息都写在这个类里面"""

    # 开启调试模式
    DEBUG = True


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
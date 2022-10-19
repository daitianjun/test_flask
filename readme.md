安装：pip install python-dotenv

.flaskenv文件 设置环境变量

from markupsafe import escape

escape 函数对路由中匹配信息转义处理
例如：

from markupsafe import escape
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

函数：端点
根据端点返回url:
from flask import url_for
url_for('user_page', name='peter')

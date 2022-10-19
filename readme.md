## 环境
安装：pip install python-dotenv
.flaskenv文件 设置环境变量

from markupsafe import escape

## escape 函数
对路由中匹配信息转义处理
例如：
from markupsafe import escape
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

## 端点&url_for
根据端点返回url:
from flask import url_for
url_for('user_page', name='peter')
print(url_for('test_url_for', num=2))  # 输出：/test?num=2


## 模板
根路径创建templates文件夹
Jinja2 的语法和 Python 大致相同，你在后面会陆续接触到一些常见的用法。在模板里，你需要添加特定的定界符将 Jinja2 语句和变量标记出来，下面是三种常用的定界符：
{{ ... }} 用来标记变量。
{% ... %} 用来标记语句，比如 if 语句，for 语句等。
{# ... #} 用来写注释。

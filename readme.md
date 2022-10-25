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

## 请求和响应
jsonify函数返回json数据
redirect函数重定向

## 端点&url_for
根据端点返回url:
from flask import url_for
url_for('user_page', name='peter')
print(url_for('test_url_for', num=2))  # 输出：/test?num=2

对于静态文件，需要传入的端点值是 static，同时使用 filename 参数来传入相对于 static 文件夹的文件路径。
例如：
<img src="{{ url_for('static', filename='foo.jpg') }}">

## 模板
根路径创建templates文件夹 默认读取
Jinja2 的语法和 Python 大致相同，你在后面会陆续接触到一些常见的用法。在模板里，你需要添加特定的定界符将 Jinja2 语句和变量标记出来，下面是三种常用的定界符：
{{ ... }} 用来标记变量。
{% ... %} 用来标记语句，比如 if 语句，for 语句等。
{# ... #} 用来写注释。

@app.context_processor装饰器添加模板上下文处理函数，注入到每一个模板

模板继承：基模板定义块，子模板继承
{% extends 'base.html' %}
{% block content %}
{% endblock %}

宏：相当于函数，减少代码重用
包含：
{% include 'header.html' %}
## 静态文件
根路径创建static文件夹 默认读取
前端将url_for 函数封装到了环境变量
## 请求钩子
装饰器
before_first_request:第一个请求之前运行 ,其实就是服务器启动后收到的第一个请求运行一次，不是每个用户的第一个请求
                     初始化数据库等操作
before_request: 处理每一个请求之前运行，记录用户最后在线时间

after_request: 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理

teardown_request:请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息

after_this_request: 装饰视图函数，请求结束之后执行

## 请求上下文


## 表单
from flask import Flask, abort, jsonify, url_for, redirect, \
    request, session
from flask import make_response
app = Flask(__name__)
# 加载配置文件
app.config.from_pyfile('config.txt')

app.secret_key = 'secret'

# 自定义响应体
@app.route('/res')
def hello():
    resp = make_response('make response测试')
    resp.headers["code"] = "Python"
    resp.status = "404 not found"
    return resp


# 错误响应
@app.route('/not_found')
def not_found():
    abort(404)

# 返回json数据
@app.route('/json')
def foo():
  return jsonify({'name': 'zhangsan', 'gender': 'male'})

# 重定向 第一个参数为端点值，
@app.route('/url_for')
def test_url_for():
    return redirect(url_for('foo', ))

# 设置cookie
@app.route('/set_cookie')
def set_cookie():
    response = make_response('设置 cookie')
    response.set_cookie('username', 'tom')
    return response

# 删除cookie
@app.route('/del_cookie')
def del_cookie():
    response = make_response('删除cookie')
    # response.set_cookie('username', '', expires=0)
    response.delete_cookie('username')
    return response

# 设置session
@app.route('/set_session')
def index1():
    session['username'] = 'tony'
    return session['username']

# 删除session
@app.route('/del_session/')
def delete():
    session.pop('username', None)
    session['username'] = False
    print(session.get('username'))
    return "删除会话"

@app.route('/')
def hello_world():
    # 获取ip
    ip = request.remote_addr
    print(ip)
    return 'Hello World!'

# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request,第一次访问之前的请求钩子")
# 每一次请求之前
@app.before_request
def before_request():
    print("before_request，每一次请求之前")

if __name__ == '__main__':
    app.run()

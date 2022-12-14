from flask import Flask, abort, jsonify, url_for, redirect, \
render_template,request

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

# 捕获错误状态码
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    # user = User.query.first()
    return render_template('404.html', user='aaa'), 404  # 返回模板和状态码

@app.route('/')
def hello_world():
    # 获取ip
    ip = request.remote_addr
    print(ip)
    return 'Hello World!'



if __name__ == '__main__':
    app.run()

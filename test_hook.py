from flask import Flask, abort, jsonify, url_for, redirect, \
    request, session, after_this_request
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request,第一次访问之前的请求钩子")


# 每一次请求之前
@app.before_request
def before_request():
    print("before_request，每一次请求之前")


# 每一次请求之后
@app.after_request
def after_request(response):
    print("after_request,每一次请求之后")
    response.status = 404
    return response


# 请每一次请求之后
@app.teardown_request
def teardown_request(e):
    print("teardown_request")


if __name__ == '__main__':
    app.run()

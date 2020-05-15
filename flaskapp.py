from flask import Flask
from flask import request
from psycopg2 import DataError, InternalError
from functools import wraps

import returnmsg
from user import *
from info import *
from moments import *

def handle_database_exception(conn):
    def handle(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except (DataError, InternalError):
                conn.rollback()
                return returnmsg.error("Database Error"), 403 #尝试SQL注入或数据不规范时会引发数据库异常，返回异常信息。
        return wrapper
    return handle

def flaskapp(cur, conn):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/test', methods=['GET', 'POST']) #TODO delete!
    def hello_world():
        if request.method == 'POST':
            data = request.get_json()
            print(data)
            return data
        if request.method == 'GET':
            json = request.args
            print(all([json.get('arg'),json.get('tes')]))
            return json
    #TODO 发生except之后把错误显示出来！！！
    @app.route('/user/register') #用户注册
    @handle_database_exception(conn)
    def register_route():
        return registerlogin.registerlogin(cur, conn, request.args)

    @app.route('/user/login') #用户登录
    @handle_database_exception(conn)
    def login_route():
        return registerlogin.registerlogin(cur, conn, request.args)


    @app.route('/user/updatetoken') #Token更新
    @handle_database_exception(conn)
    def updatetoken_route():
        return updatetoken.updatetoken(cur, conn, request.args)


    @app.route('/user/getselfinfo') #获取个人信息
    @handle_database_exception(conn)
    def getselfinfo_route():
        return getselfinfo.getselfinfo(cur, request.args)


    @app.route('/user/getpublicinfo') #获取用户公众信息
    @handle_database_exception(conn)
    def getpublicinfo_route():
        return getpublicinfo.getpublicinfo(cur, request.args)


    @app.route('/user/updatedata', methods=["POST"]) #更新个人信息
    @handle_database_exception(conn)
    def updatedata_route():
        return updatedata.updatedata(cur, conn, request.get_json())


    @app.route('/info/getstatistic') #获取历史数据
    @handle_database_exception(conn)
    def getstatistic_route():
        return getstatistic.getstatistic(cur, request.args)


    @app.route('/info/poststatistic', methods=["POST"]) #更新数据
    @handle_database_exception(conn)
    def poststatistic_route():
        return poststatistic.poststatistic(cur, conn, request.get_json())


    @app.route('/moments/getmomentsid') #获取`id为xxxx用户`或者`全体用户`的所有MomentsID
    @handle_database_exception(conn)
    def getmomentsid_route():
        return getmomentsid.getmomentsid(cur, request.args)


    @app.route('/moments/getmoment') #获取单条动态内容
    @handle_database_exception(conn)
    def getmoment_route():
        return getmoment.getmoment(cur, request.args)


    @app.route('/moments/thumbup') #点赞
    @handle_database_exception(conn)
    def thumbup_route():
        return thumbup.thumbup(cur, conn, request.args)


    @app.route('/moments/postmoment', methods=["POST"]) #发动态
    @handle_database_exception(conn)
    def postmoment_route():
        return postmoment.postmoment(cur, conn, request.get_json())


    @app.route('/moments/postcomment', methods=["POST"]) #评论
    @handle_database_exception(conn)
    def postcomment_route():
        return postcomment.postcomment(cur, conn, request.get_json())

    
    # @app.handle_exception()
    # @app.errorhandler()
    def null(): #TODO 看看怎么用上面两个东西
        pass

    app.run() #TODO debugging
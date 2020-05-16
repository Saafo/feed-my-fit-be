import json
from flask import Flask
from flask import request
from flask import g
from psycopg2 import DataError, InternalError
from functools import wraps

import returnmsg
import database
from user import *
from info import *
from moments import *
from rank import *

def handle_database_exception():
    def handle(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except (DataError, InternalError):
                g.conn.rollback()
                return returnmsg.error("Database Error", 403) #尝试SQL注入或数据不规范时会引发数据库异常，返回异常信息。
        return wrapper
    return handle

#数据库信息
config = {}
with open('./config.json') as f:
    config = json.load(f)

username = config['database']['username']
password = config['database']['password']
basename = config['database']['basename']
hostname = config['database']['hostname']
port = config['database']['port']

mybase = database.Postgres(username,password,basename,hostname,port)


app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.before_request
def before_request():
    mybase.connect()
    mybase.cursor()
    g.cur = mybase.cur
    g.conn = mybase.conn

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'conn'):
        g.conn.close()

# route part

@app.route('/user/register') #用户注册
@handle_database_exception()
def register_route():
    return registerlogin.registerlogin(g.cur, g.conn, request.args)

@app.route('/user/login') #用户登录
@handle_database_exception()
def login_route():
    return registerlogin.registerlogin(g.cur, g.conn, request.args)


@app.route('/user/updatetoken') #Token更新
@handle_database_exception()
def updatetoken_route():
    return updatetoken.updatetoken(g.cur, g.conn, request.args)


@app.route('/user/getselfinfo') #获取个人信息
@handle_database_exception()
def getselfinfo_route():
    return getselfinfo.getselfinfo(g.cur, request.args)


@app.route('/user/getpublicinfo') #获取用户公众信息
@handle_database_exception()
def getpublicinfo_route():
    return getpublicinfo.getpublicinfo(g.cur, request.args)


@app.route('/user/updatedata', methods=["POST"]) #更新个人信息
@handle_database_exception()
def updatedata_route():
    return updatedata.updatedata(g.cur, g.conn, request.get_json())


@app.route('/info/getstatistic') #获取历史数据
@handle_database_exception()
def getstatistic_route():
    return getstatistic.getstatistic(g.cur, request.args)


@app.route('/info/poststatistic', methods=["POST"]) #更新数据
@handle_database_exception()
def poststatistic_route():
    return poststatistic.poststatistic(g.cur, g.conn, request.get_json())


@app.route('/moments/getmomentsid') #获取`id为xxxx用户`或者`全体用户`的所有MomentsID
@handle_database_exception()
def getmomentsid_route():
    return getmomentsid.getmomentsid(g.cur, request.args)


@app.route('/moments/getmoment') #获取单条动态内容
@handle_database_exception()
def getmoment_route():
    return getmoment.getmoment(g.cur, request.args)


@app.route('/moments/thumbup') #点赞
@handle_database_exception()
def thumbup_route():
    return thumbup.thumbup(g.cur, g.conn, request.args)


@app.route('/moments/postmoment', methods=["POST"]) #发动态
@handle_database_exception()
def postmoment_route():
    return postmoment.postmoment(g.cur, g.conn, request.get_json())


@app.route('/moments/postcomment', methods=["POST"]) #评论
@handle_database_exception()
def postcomment_route():
    return postcomment.postcomment(g.cur, g.conn, request.get_json())

@app.route('/rank/dailyscore') #每日健康值排行榜
@handle_database_exception()
def dailyscore_route():
    return dailyscore.dailyscore(g.cur, request.args)

@app.route('/rank/streak') #连击排行榜
@handle_database_exception()
def streak_route():
    return streak.streak(g.cur, request.args)


@app.errorhandler(404)
def page_not_found(e): 
    return returnmsg.notfound()
    
@app.errorhandler(Exception)
def handle_exception(e):
    print(e)
    return returnmsg.internalerror()

if __name__ == "__main__":
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
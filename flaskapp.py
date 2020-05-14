from flask import Flask
from flask import request

from user import *
from info import *
from moments import *

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

    @app.route('/user/register') #用户注册
    def register_route():
        try:
            return registerlogin.registerlogin(cur, conn, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY" #尝试SQL注入时会引发异常，返回异常信息。

    @app.route('/user/login') #用户登录
    def login_route():
        try:
            return registerlogin.registerlogin(cur, conn, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/user/updatetoken') #Token更新
    def updatetoken_route():
        try:
            return updatetoken.updatetoken(cur, conn, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/user/getselfinfo') #获取个人信息
    def getselfinfo_route():
        try:
            return getselfinfo.getselfinfo(cur, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/user/getpublicinfo') #获取用户公众信息
    def getpublicinfo_route():
        try:
            return getpublicinfo.getpublicinfo(cur, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/user/updatedata', methods=["POST"]) #更新个人信息
    def updatedata_route():
        try:
            return updatedata.updatedata(cur, conn, request.get_json())
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/info/getstatistic') #获取历史数据
    def getstatistic_route():
        try:
            return getstatistic.getstatistic(cur, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/info/poststatistic', methods=["POST"]) #更新数据
    def poststatistic_route():
        try:
            return poststatistic.poststatistic(cur, conn, request.get_json())
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/moments/getmomentsid') #获取`id为xxxx用户`或者`全体用户`的所有MomentsID
    def getmomentsid_route():
        try:
            return getmomentsid.getmomentsid(cur, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/moments/getmoment') #获取单条动态内容
    def getmoment_route():
        try:
            return getmoment.getmoment(cur, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/moments/thumbup') #点赞
    def thumbup_route():
        try:
            return thumbup.thumbup(cur, conn, request.args)
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/moments/postmoment', methods=["POST"]) #发动态
    def postmoment_route():
        try:
            return postmoment.postmoment(cur, conn, request.get_json())
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    @app.route('/moments/postcomment', methods=["POST"]) #评论
    def postcomment_route():
        try:
            return postcomment.postcomment(cur, conn, request.get_json())
        except Exception:
            conn.rollback()
            return "FUCKYOUSCRIPTBOY"

    app.run() #TODO debugging
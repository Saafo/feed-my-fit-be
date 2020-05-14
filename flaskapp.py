from flask import Flask
from flask import request

from user import *
from info import *
from moments import *

def flaskapp(mybase):
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

    #TODO 所有route都要做个参数完整性验证
    @app.route('/user/register') #用户注册
    def register_route():
        return registerlogin.registerlogin(mybase, request.args)

    @app.route('/user/login') #用户登录
    def login_route():
        return registerlogin.registerlogin(mybase, request.args)

    @app.route('/user/updatetoken') #Token更新
    def updatetoken_route():
        return updatetoken.updatetoken(mybase, request.args)

    @app.route('/user/getselfinfo') #获取个人信息
    def getselfinfo_route():
        return getselfinfo.getselfinfo(mybase, request.args)

    @app.route('/user/getpublicinfo') #获取用户公众信息
    def getpublicinfo_route():
        return getpublicinfo.getpublicinfo(mybase, request.args)

    @app.route('/user/updatedata', methods=["POST"]) #更新个人信息
    def updatedata_route():
        return updatedata.updatedata(mybase, request.get_json())

    @app.route('/info/getstatistic') #获取历史数据
    def getstatistic_route():
        return getstatistic.getstatistic(mybase, request.args)

    @app.route('/info/poststatistic', methods=["POST"]) #更新数据
    def poststatistic_route():
        return poststatistic.poststatistic(mybase, request.get_json())

    @app.route('/moments/getmomentsid') #获取`id为xxxx用户`或者`全体用户`的所有MomentsID
    def getmomentsid_route():
        return getmomentsid.getmomentsid(mybase, request.args)

    @app.route('/moments/getmoment') #获取单条动态内容
    def getmoment_route():
        return getmoment.getmoment(mybase, request.args)

    @app.route('/moments/thumbup') #点赞
    def thumbup_route():
        return thumbup.thumbup(mybase, request.args)

    @app.route('/moments/postmoment', methods=["POST"]) #发动态
    def postmoment_route():
        return postmoment.postmoment(mybase, request.get_json())

    @app.route('/moments/postcomment', methods=["POST"]) #评论
    def postcomment_route():
        return postcomment.postcomment(mybase, request.get_json())

    app.run() #TODO debugging
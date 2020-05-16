def success(data):
    return {'errorCode':0, 'errorMsg':'ok','data':data}

def empty(msg):
    return {'errorCode':-1, 'errorMsg':msg}, 404

def error(msg, state):
    return {'errorCode':-2, 'errorMsg':msg}, state

def tokeninvalid():
    return {'errorCode':-3, 'errorMsg':'Token过期或不合法，请重新登录'}, 401

def notfound():
    return {'errorCode':-4, 'errorMsg':'invalid url'}, 404

def internalerror():
    return {'errorCode':-5, 'errorMsg':'服务器内部错误，请联系管理员'}, 500
def success(data):
    return {'errorCode':0, 'errorMsg':'ok','data':data}

def empty(msg):
    return {'errorCode':-1, 'errorMsg':msg}

def error(msg):
    return {'errorCode':-2, 'errorMsg':msg}, 400

def tokeninvalid():
    return {'errorCode':-3, 'errorMsg':'Token过期或不合法，请重新登录'}, 401
# about getmoment
import userToken
import returnmsg

def getmoment(mybase, args):
    id = args.get('id')
    token = args.get('token')
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    momentid = args.get('momentid')
    #TODO 从数据库中获取momentid的数据

    return returnmsg.success(data)
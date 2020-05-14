# about getmoment
import userToken
import returnmsg

def getmoment(mybase, args):
    id = args.get('id')
    token = args.get('token')
    momentid = args.get('momentid')
    #参数完整性验证
    if all([id, token, momentid]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    #TODO 从数据库中获取momentid的数据

    return returnmsg.success(data)
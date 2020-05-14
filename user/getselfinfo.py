# about user getselfinfo
import userToken
import returnmsg

def getselfinfo(mybase, args):
    id = args.get('id')
    token = args.get('token')
    #参数完整性验证
    if all([id, token]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    #TODO 连接数据库，获取信息

    data = {} #TODO 填充data
    return returnmsg.success(data)
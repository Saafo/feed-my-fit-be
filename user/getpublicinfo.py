# about user getpublicinfo
import userToken
import returnmsg

def getpublicinfo(cur, args):
    id = args.get('id')
    token = args.get('token')
    getid = args.get('getid')
    #参数完整性验证
    if all([id, token, getid]) == False:
        return returnmsg.error('参数不完整')

    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()


    #TODO 连接数据库，获取信息

    #如果用户存在
    data = {} #TODO 填充data
    return returnmsg.success(data)

    #如果用户不存在
    return returnmsg.error('用户不存在')
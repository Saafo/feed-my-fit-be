# about thumbup
import userToken
import returnmsg

def thumbup(mybase, args):
    id = args.get('id')
    token = args.get('token')
    momentid = args.get('momentid')
    #参数完整性验证
    if all([id, token, momentid]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()

    #TODO 数据库找到momentid, thumb+1

    return returnmsg.success({})
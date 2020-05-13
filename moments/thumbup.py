# about thumbup
import userToken
import returnmsg

def thumbup(mybase, args):
    id = args.get('id')
    token = args.get('token')
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()

    momentid = args.get('momentid')

    #TODO 数据库找到momentid, thumb+1

    return returnmsg.success({})